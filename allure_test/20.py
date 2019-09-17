import allure, os,sys


sys.path.insert(0,r"C:\\Users\\Administrator\\Desktop\\关于网站\\ccc\\爬虫系统\\go\\allure_test")
from allure_test import methods


class Test_20:
    def setup_class(self):
        methods.max_window()

    def teardown_class(self):
        methods.close()

    @allure.feature('打开京东')
    @allure.story('点击登陆')
    def test_case_15(self):
        '''用例名称京东-登录-百度-新闻-百度'''
        methods.get_url("https://www.jd.com", desc="打开京东")
        methods.click("xpath=>//*[contains(text(),'请登录')]", desc="登陆")
        methods.click("xpath=>//*[contains(text(),'账户登录')]", desc="切换账户登陆")
        methods.send_key("xpath=>//*[@id='loginname']", 188888888, desc="发送账户名密码")
        methods.wait(5)

    @allure.feature('打开京东')
    @allure.story('点击登陆')
    def test_case_16(self):
        '''用例名称京东-登录-百度-新闻-百度'''
        methods.get_url("https://www.jd.com", desc="打开京东")
        methods.click("xpath=>//*[contains(text(),'请登录')]", desc="登陆")
        methods.click("xpath=>//*[contains(text(),'账户登录')]", desc="切换账户登陆")
        methods.send_key("xpath=>//*[@id='loginname']", 188888888, desc="发送账户名密码")
        methods.wait(5)

    # @allure.feature('京东-百度-删除-创建15 16 17')
    # @allure.story('自动平台登录公众脚本-点击删除等')
    # def test_case_16(self):
    #     '''自动测试平台脚本/删除'''
    #
    #     methods.get_url("https://www.baidu.com", desc="get_url_百度")
    #     methods.click("xpath=>//*[contains(text(),'新闻')]", desc="点击新闻")
    #     methods.click("xpath=>//*[contains(text(),'百度首页')]", desc="点击百度首页")

