from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service(ChromeDriverManager(cache_valid_range=30).install())
driver = webdriver.Chrome(service=service)
