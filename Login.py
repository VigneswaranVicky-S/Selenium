import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
username = "standard_user"
password = "secret_sauce"
login_url = "https://www.saucedemo.com/v1/"
driver.get(login_url)

time.sleep(3)

username_filed = driver.find_element(By.ID,"user-name")
password_filed = driver.find_element(By.ID,"password")

username_filed.send_keys(username)
password_filed.send_keys(password)

login_button = driver.find_element(By.ID,"login-button")
login_button.click()
time.sleep(3)
driver.quit()

