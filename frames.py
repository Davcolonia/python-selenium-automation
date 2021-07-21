from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.implicitly_wait(2)

# open url
driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe')

# switch to frame 1
driver.switch_to.frame('iframeResult')

# switch to frame 2
frame = driver.find_element(By.CSS_SELECTOR, "iframe[src='https://www.w3schools.com']")
driver.switch_to.frame(frame)

# find a logo
logo = driver.find_element(By.CSS_SELECTOR, "a.w3-bar-item[title='Home']")

# verify it switched
print(logo.get_attribute('href'))

assert 'https://www.w3schools.com/' == logo.get_attribute('href')

driver.quit()