import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

"""
class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)
    
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()
    
"""

class RobloxLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        driver = self.driver
        driver.get("https://www.roblox.com/login")
        username = driver.find_element(By.ID, "login-username")
        password = driver.find_element(By.ID, "login-password")
        logIn = driver.find_element(By.ID, "login-button")
        
        username.send_keys("NoobCaster678")
        password.send_keys("christianCL203195!")
        logIn.click()
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()