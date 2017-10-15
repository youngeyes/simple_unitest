#-*-coding:utf-8-*-
from selenium import webdriver
from auto_zentao import Zentao
from HTMLTestRunner import HTMLTestRunner
import unittest
class Test_unit(unittest.TestCase):
    def setUp(self):
        print("test start")
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.0.185/zentao/user-login.html")
    def test_login(self):
        # 登录
        zentao = Zentao(self.driver)  # 实例化类
        self.assertEqual(zentao.login("admin", "Qwe123"), "我的地盘 - 禅道")
    def test_createproduct(self):
        zentao = Zentao(self.driver)
        zentao.login("admin", "Qwe123")
        productname = "product3"
        productcode = "code3"
        self.assertEqual(zentao.createproduct(productname,productcode),"product3"+"::浏览产品 - 禅道")
    def tearDown(self):
        print("test end")
if __name__=="__main__":
    testuint=unittest.TestSuite()
    testuint.addTest(Test_unit("test_login"))
    testuint.addTest(Test_unit("test_createproduct"))
    fr = open('d:/testresult.html','wb')
    runner = HTMLTestRunner(stream=fr,title='报告',description='用例执行情况')
    runner.run(testuint)
    fr.close()