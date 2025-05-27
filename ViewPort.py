from selenium import webdriver
import time

viewports = [(375,667),(1024,1366),(344,882),(412,915)]

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/webhp?authuser=9")

try:
    for width,height in viewports:
        driver.set_window_size(width,height)
        time.sleep(4)
finally:
    driver.close()