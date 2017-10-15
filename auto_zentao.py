#-*-coding:utf-8-*-
from time import sleep
class Zentao():
    def __init__(self,driver):
        self.driver = driver

    def login(self,username,password):
        self.driver.find_element_by_css_selector("#account").send_keys(username)
        sleep(2)
        self.driver.find_element_by_css_selector("[name='password']").send_keys(password)
        sleep(2)
        self.driver.find_element_by_css_selector("#submit").click()
        return self.driver.title
    def logout(self):
        self.driver.find_element_by_link_text("退出").click()
        self.driver.close()

    def createproduct(self,productname,productcode):
        # 添加产品
        self.driver.find_element_by_link_text("产品").click()
        sleep(2)
        self.driver.find_element_by_css_selector("[data-id='create']>a").click()
        self.driver.find_element_by_css_selector("#name").send_keys(productname)
        sleep(2)
        self.driver.find_element_by_css_selector("#code").send_keys(productcode)
        self.driver.find_element_by_css_selector("#submit").submit()
        return self.driver.title
        # if title_pro == productname+"::浏览产品 - 禅道":
        #     print("product add success")
        # else:
        #     print("product add fail")

