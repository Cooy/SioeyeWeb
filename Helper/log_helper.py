#coding:utf-8
#CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET

import logging
from common_Helper import *
import os

def get_logger(level='INFO',cases=None):
    '''

    :param level: 'CRITICAL','ERROR','WARNING','INFO','DEBUG','NOTESET'
    :return:logger
    '''
    ftime = get_time()
    logger = logging.getLogger(cases)
    logger.setLevel(getattr(logging, level))
    #create a console
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # create a file handler
    check_path()
    handler = logging.FileHandler("./logs/"+ftime+'Sioeye.log')
    #handler.setLevel(logging.INFO)
    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(handler)
    logger.addHandler(console)
    logger.propagate=True
    return logger

def check_path(path='./'):
    for filename in os.listdir(path):
        if filename == "logs":
            break
    else:
        os.mkdir('./' + '/logs')