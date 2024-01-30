from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from assertpy import soft_assertions, assert_that

driver= webdriver.Chrome()

driver.get("https://practicetestautomation.com/practice-test-login/")

wait = WebDriverWait(driver, 10)

username = driver.find_element(By.ID,"username")
password = driver.find_element(By.ID,"password")
submitButton = driver.find_element(By.ID,"submit")

username.send_keys("student")
password.send_keys("Password123")
submitButton.click()


title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.post-title")))

with soft_assertions():
   assert_that(title).is_true()





