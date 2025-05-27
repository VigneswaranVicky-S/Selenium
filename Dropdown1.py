from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
login_url = ("https://the-internet.herokuapp.com/dropdown")
driver.get(login_url)

dropdown = driver.find_element(By.ID,"dropdown")
# select = Select(dropdown)
# select.select_by_visible_text("Option 1")
# select.select_by_index(2)
# select.select_by_value("2")
# option_count = len(select.options)
# expected_count =3
# if option_count == expected_count:
    # print("test case passed successfully and count is correct")
# else:
    # print("test case failed and count is incorrect")

target_value = "Option 2"
select = Select(dropdown)
for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"selected option is {target_value}")
        break
    else:
        print(f"option '{target_value}' not found")

