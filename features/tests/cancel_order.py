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
driver.find_element(By.ID,'helpsearch').send_keys('Cancel order', Keys.ENTER)
actual_text = driver.find_element(By.XPATH, "//div[@class='help-content']//h1").text
expected_result = 'Cancel Items or Orders'

# wait for 4 sec
sleep(4)

# click search

# verify
assert expected_result == actual_text, f"Expected {expected_result}, but got {actual_text}"
driver.quit()
