from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/")
driver.switch_to.new_window()
driver.get("https://playwright.dev/")
number_of_tabs = len(driver.window_handles)
print(number_of_tabs)
tabs_value = driver.window_handles
print(tabs_value)
current_tab = driver.current_window_handle
print(current_tab)
driver.find_element(By.CSS_SELECTOR,".getStarted_Sjon").click()
first_tab = driver.window_handles[1]
# if current_tab != first_tab:
driver.switch_to.window(first_tab)
driver.find_element(By.XPATH,"//h4[normalize-space()='Selenium Grid']").click()