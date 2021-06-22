from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
driver = webdriver.Chrome(executable_path='/Users/hdl32da01/python-selenium-automation/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.amazon.com/')
driver.find_element(By.ID,'twotabsearchtextbox').send_keys('Table')
e = driver.wait.until(EC.element_to_be_clickable((By.ID, 'nav-search-submit-button')))
e.click()
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

print(f'Actual result: {actual_result}')
expected_result = '"Table"'

# wait for 4 sec
# sleep(4)
driver.implicitly_wait(4)
# click search

# verify
assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
driver.quit()
