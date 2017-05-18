# coding=utf-8


import os
import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from appium.webdriver.common.touch_action import TouchAction
import sys; sys.path.insert(0, '../Module/Module')




class KONOAndroidTests(unittest.TestCase):
    
    def setUp(self):
        desired_caps = {}
        desired_caps['appium-version'] = '1.0'
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '10.2'
        desired_caps['deviceName'] = 'iPhone 7'
        desired_caps['app'] = os.path.abspath('/Users/kono/Desktop/sample-code-master 2/Kono.app')
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)


    def test_1_Find_Stars(self):
        try:
            print("time.sleep(20)")
            time.sleep(30)
            try:
                print("tap Allow")
                self.driver.find_element_by_accessibility_id("Allow").click()
            except:
                print("already handle by last time")
            
            email="mingshing.kuo+106@thekono.com"
            password="a"
            print("loginRegister")
            time.sleep(10)
            self.driver.find_element_by_accessibility_id("loginRegister").click()
            print("Log in with Email")
            time.sleep(10)
            self.driver.find_element_by_accessibility_id("Sign Up").click()
            time.sleep(10)
            self.driver.find_element_by_accessibility_id("Sign up with Email").click()
            time.sleep(10)
            self.driver.find_element_by_accessibility_id("Email").send_keys(email)
            self.driver.find_element_by_accessibility_id("Password").send_keys(password)
            self.driver.find_element_by_accessibility_id("Confirm Password").send_keys(password)
            self.driver.find_element_by_accessibility_id("return").click()
            time.sleep(20)
            #self.driver.find_element_by_accessibility_id("Sign Up").click()
            time.sleep(10)
            self.driver.find_element_by_accessibility_id("OK").click()
            time.sleep(10)
            self.driver.find_element_by_accessibility_id("Most Popular").click()
            self.driver.find_element_by_xpath("xpath: //XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]").click()
            print("script successful , close app")
            self.driver.quit()
    
        except:
            print("script unsuccessful , close app")
            self.driver.quit()

        


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(KONOAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
