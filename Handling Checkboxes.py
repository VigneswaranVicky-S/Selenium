import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://practice.expandtesting.com/checkboxes#google_vignette')
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()

checked_count =0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count +=1

expected_checked_count = 2

if checked_count == expected_checked_count:
    print('checkbox count verified')
else:
    print('checkbox count mismatch')

time.sleep(5)
driver.close()



