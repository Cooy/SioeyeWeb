#coding:utf-8

from SioeyeLive.LiveUtils.main_util import *
from SioeyeLive.Pages.main_page import *
from Helper.log_helper import *
import time
import unittest
class TestMain(unittest.TestCase):

    path = MainCssPath()
    logger = get_logger('DEBUG',cases='TestMain')

    def setUp(self):
        self.util = MainUtil()
        self.util.open_live_page()

    def tearDown(self):
        self.util.quit()

    def test_openLive(self):
        '''
        usage:测试打开live界面
        :return:
        '''
        expect=self.path.URL
        actual=self.util.get_url()
        self.logger.debug('expect URL = ' + expect)
        self.logger.debug('actual URL = ' + actual)
        self.assertEqual(expect,actual,expect+'does not match'+actual)

    def test_title(self):
        '''
        usage：测试title是否符合预期
        :return:
        '''
        expect=self.path.TITLE.decode('utf-8')
        actual=self.util.get_title()
        self.logger.debug('expect TITLE = '+expect)
        self.logger.debug('actual TITLE = '+actual)
        self.assertEqual(expect,actual,expect+'does not match'+actual)

    def test_login(self):
        self.util.click_lojo()
        self.util.in_username()
        self.util.in_password()
        self.util.click_login()
        time.sleep(4)
        expect=self.path.DISCOVER_TITLE.decode('utf-8')
        actual=self.util.get_title()
        self.logger.debug('expect TITLE = '+expect)
        self.logger.debug('actual TITLE = '+actual)
        self.assertEqual(expect,actual,expect+'does not match'+actual)


if __name__ == '__main__':

#    unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(TestMain("test_login"))
    testunit.addTest(TestMain("test_title"))
    testunit.addTest(TestMain("test_openLive"))
    runner = unittest.TextTestRunner()
    runner.run(testunit)






