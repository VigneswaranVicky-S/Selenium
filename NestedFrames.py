from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/nested_frames")

# Switching to Top Frame

driver.switch_to.frame("frame-top")

# Switching to Middle frame

driver.switch_to.frame("frame-middle")
content = driver.find_element(By.ID,"content").text
print("content in middle frame", content)

# Switching to Default content

driver.switch_to.default_content()

# Switching to Bottom Frame

driver.switch_to.frame("frame-bottom")

bottom = driver.find_element(By.TAG_NAME,"body").text
print("Content in bottom frame", bottom)