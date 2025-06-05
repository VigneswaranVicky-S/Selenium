import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()
url = "https://the-internet.herokuapp.com/javascript_alerts"
browser.get(url)
alert_button = browser.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
alert_button.click()
alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)
time.sleep(5)
alert.send_keys("Selenium with python")
time.sleep(5)
alert.dismiss()