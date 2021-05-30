from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# init driver
driver = webdriver.Chrome(executable_path='/Users/hdl32da01/python-selenium-automation/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')
actual_result = driver.find_element(By.ID,'helpsearch').send_keys('Cancel order', Keys.ENTER)

print(f'Actual result: {actual_result}')
# @LANA What would our expected result be in for this case? would it be None?
expected_result = '"Cancel order"'

# wait for 4 sec
sleep(4)

# click search

# verify
assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
driver.quit()
