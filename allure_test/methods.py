import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import allure


byTypeDict = {
    "xpath": By.XPATH,
    "id": By.ID,
    "name": By.NAME,
    "class_name": By.CLASS_NAME,
    "tag_name": By.TAG_NAME,
    "link_text": By.LINK_TEXT,
    "partial_link_text": By.PARTIAL_LINK_TEXT,
    "css selector" : By.CSS_SELECTOR
}

driver = webdriver.Chrome(executable_path='C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe')
# 获取单个页面元素
def getElement(loc):
    try:
        by = loc.split("=>")[0]
        value = loc.split("=>")[1]
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element(by=byTypeDict[by], value=value))
        # print(element)
        return element
    except Exception as e:
        raise e

# 获取一组相同的元素，以列表形式返回
def getElements(loc):
    try:
        by = loc.split("=>")[0]
        value = loc.split("=>")[1]
        elements = WebDriverWait(driver, 5).until(lambda x: x.find_elements(by=byTypeDict[by], value=value))
        return elements
    except Exception as e:
        raise e

def get_url(*args, desc=None):
    with allure.step(desc):
        try:
            driver.get(args[0])
        except Exception as e:
            raise e

def wait(*args, desc=None):
    with allure.step(desc):
        try:
            time.sleep(args[0])
        except Exception as e:
            raise e

def max_window(*args, **kwargs):
    try:
        driver.maximize_window()
    except Exception as e:
        raise e

def close(desc=None):
    with allure.step(desc):
        try:
            driver.quit()
        except Exception as e:
            raise e

def click(loc,desc=None):
    with allure.step(desc):
        try:
            print("这里是点击方法")
            getElement(loc).click()
        except Exception as e:
            raise e

def send_key(loc,key,desc=None):
    with allure.step(desc):
        try:
            getElement(loc).send_keys(Keys.CONTROL,'a')
            getElement(loc).send_keys(key)
        except Exception as e:
            raise e



def enter(desc=None):
    with allure.step(desc):
        try:
            ActionChains(driver).send_keys(Keys.ENTER).perform()
        except Exception as e:
            raise e




def down(desc=None):
    with allure.step(desc):
        try:
            ActionChains(driver).send_keys(Keys.DOWN).perform()
        except Exception as e:
            raise e

def get_text(loc,desc=None):
    with allure.step(desc):
        try:
            return getElement(loc).text
        except Exception as e:
            raise e

def assert_str1_in_str2(loc,text,desc=None):
    with allure.step(desc):
        try:
            assert text in get_text(loc)
        except Exception as e:
            raise e

def selectOption(loc,text,desc=None):
    with allure.step(desc):
        global driver
        try:
            s = Select(getElement(loc))
            selector = text.split("=")
            if selector[0] == "index":
                s.select_by_index(int(selector[1]))
            elif selector[0] == "value":
                s.select_by_value(selector[1])
            elif selector[0] == "text":
                s.select_by_visible_text(selector[1])
        except Exception as e:
            raise e

def alertOperate(*args,desc=None):
    with allure.step(desc):
        try:
            alert = driver.switch_to.alert
            if args[0] == "确定":
                alert.accept()
            else:
                alert.dismiss()
        except Exception as e:
            raise e

def click_word(word,desc=None):
    with allure.step(desc):
        try:
            # value = "//*[text()='"+word+"']"
            # value = "//*[@class='" + word +"']"
            loc = "xpath=>//*[contains(text(),'"+word+"')]"
            print(loc)
            getElement(loc).click()
        except Exception as e:
            raise e

