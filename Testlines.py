#_*_ coding:utf-8 _*_
'''
Created on 2017年5月20日

@author: lch
'''

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.google.com")


print ("设置浏览器宽480、高800显示")
driver.set_window_size(1000, 800)
driver.quit()