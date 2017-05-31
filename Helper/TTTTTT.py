#coding:utf-8
import unittest


from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.find_element_by_class_name('login').click()
driver.find_element_by_class_name('login').send_keys('sioeye@qq.com')

driver.find_element_by_class_name('/html/body/header/div/div[1]/a[1]').is_displayed()


driver.get('http://www.baidu.com')
time.sleep(5)
driver.quit()




