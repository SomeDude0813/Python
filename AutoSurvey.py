import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

'''
Opens the branded surveys website and logs in with the given user and password
Automatically finds a survey and fills out the questions

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Option A: Use partial link text if exact match fails
beginsurvey = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Survey")))

# Option B: Use XPath if it's not a standard <a> tag or text varies
# This finds any element containing the text "Take Survey"
beginsurvey = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Take Survey')]")))

'''

EMAIL = "cc7474766@gmail.com"
PASSWORD = "081388881pO"



class AutoSurvey(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test_survey(self):
        driver = self.driver
        driver.get("https://surveys.gobranded.com/users/login/") # Initialize the browser
        wait = WebDriverWait(driver, 10) # Wait up to 10 seconds for the elemnt to be clickable
        
        login_email = driver.find_element(By.NAME, "email")
        login_password = driver.find_element(By.NAME, "password")
        
        login_email.send_keys(EMAIL) # Inputs the email
        login_password.send_keys(PASSWORD) # Inputs the password
        
        button = driver.find_element(By.CSS_SELECTOR, ".submit")
        button.click()
        
        wait = WebDriverWait(driver, 20)
        
        
        beginsurvey = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Take Survey')]"))).click()
        
        beginsurvey = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Take Survey')]"))).click()
        
        question1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-id='question1']")))
        
        
    def tearDown(self):
        return
        #self.driver.close()
        
if __name__ == "__main__":
    unittest.main()

