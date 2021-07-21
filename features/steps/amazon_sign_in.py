from time import sleep
from selenium import webdriver
#from selenium.webdriver.common.by import By

# init driver
# driver = webdriver.Chrome(executable_path='/Users/hdl32da01/python-selenium-automation/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)

# open the url
#driver.get('https://www.amazon.com/')
# find logo
#logo_locator = driver.find_element(By.XPATH, "//span[@class='a-icon a-icon0logo']").text
# find email
#email_locator = driver.find_element(By.ID, 'ap_email').send_keys('testaccount@gmail.com')
# find continue button
#continue_locator = driver.find_element(By.ID, 'continue').click()
# find help link
#help_link_locator = driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()
# find forgot password
#forgot_password_locator = driver.find_element(By.ID, 'auth-fpp-link-bottom').click()
# find 'other issues with sign in link'
#sign_in_issues_locator = driver.find_element(By.ID, 'ap-other-signin-issues-link').click()
# find create account
#create_account_locator = driver.find_element(By.ID, 'create-AccountSubmit').click()
# find conditions of use
#create_conditions_locator = driver.find_element(By.LINK_TEXT, '/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088').click()
# find privacy policy
#create_privacy_policy_locator = create = driver.find_element(By.LINK_TEXT, '/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496').click()
# code wars kata
#def past(h, m, s):
#   return (h*3600 + m*60 + s) * 1000