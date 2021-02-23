#!/usr/bin/python3
# -*- coding: utf-8 -*-


from selenium import webdriver

browser = webdriver.Chrome('./chromedriver')
browser.get("http://s.wanfangdata.com.cn/paper?q=%E5%90%88%E6%88%90%E7%94%9F%E7%89%A9%E5%AD%A6")


while True:
    # 切换到iframe中
    # 获取 iframe 对象
    iframe_elemnt = browser.find_element_by_id("loginframe")
    browser.switch_to.frame(iframe_elemnt)


    elements = browser.find_elements_by_xpath('//div[@title="2021"]/span')
    for element in elements:
        title = element.find_element_by_css_selector('.words').text
        author = element.find_element_by_css_selector('amount').text
        print(author,"=>",title)
    


browser.quit()
