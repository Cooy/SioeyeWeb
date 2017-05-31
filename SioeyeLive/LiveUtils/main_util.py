#coding:utf-8

from Helper.webdriver_helper import *
from SioeyeLive.Pages.main_page import *
class MainUtil(Pyse):

    path = MainCssPath()
    def __init__(self):
        super(MainUtil, self).__init__()

    def open_live_page(self):

        '''
        open sioeye live page
        :return:
        '''
        self.open(self.path.URL)

    def click_lojo(self):
        '''
        usage:click login&&joing button
        :return:
        '''
        self.click('css=>'+self.path.LOGINJOIN)

    def in_username(self,username=path.USERNAME):
        '''
        usage:in login page,input username
        :return:
        '''
        self.type('css=>'+self.path.LOGIN_USERNAME,username)
    def in_password(self,password=path.PASSWORD):
        '''
        usage:in login page,input password
        :param password:
        :return:
        '''
        self.type('css=>'+self.path.LOGIN_PASSWORD,password)
    def click_login(self):
        '''
        usage:click login button
        :return:
        '''
        self.click('css=>'+self.path.SUBLOGIN)

#if __name__ == '__main__':
#    MainUtil().open_live_page()