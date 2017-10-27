# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

'''
模拟登陆CSDN：http://cuiqingcai.com/2599.html
'''
def login_csdn():
    # 需要下载geckodriver.exe, 并将其解压目录放到PATH中，否则容易找不到驱动（https://stackoverflow.com/questions/29858752/error-message-chromedriver-executable-needs-to-be-available-in-the-path）
    # selenium(3.4.3), Firefox(55.0.3 (32 位)), geckodriver.exe(v0.18.0, https://github.com/mozilla/geckodriver)
    driver = webdriver.Firefox()
    try:
        driver.get("https://passport.csdn.net/account/login")

        # 根据id获取元素
        elem_user = driver.find_element_by_id("username")
        elem_user.send_keys("oldinaction@qq.com")
        elem_pwd = driver.find_element_by_id("password")
        elem_pwd.send_keys("xxxxx")
        elem_pwd.send_keys(Keys.RETURN)

        time.sleep(5)
        # 如果判断出错则抛出异常
        assert "CSDN" in driver.title
    except (AssertionError, Exception) as e:
        print e
    finally:
        # 关闭driver进程(关闭浏览器)
        if driver is not None:
            driver.quit()

if __name__ == '__main__':
    login_csdn()