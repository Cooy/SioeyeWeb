#coding:utf-8
import time
import unittest

def get_time():
    '''
    :return:now time
    '''
    return time.strftime("%Y-%m-%d %H%M", time.localtime())

def get_cases(test_dir='./',top_level_dir=None):
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(
        test_dir,pattern='test*.py',top_level_dir=top_level_dir)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
    return testunit


if __name__ == '__main__':
    get_cases()