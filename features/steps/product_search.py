from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')

# init driver
driver = webdriver.Chrome(executable_path='/Users/hdl32da01/python-selenium-automation/chromedriver.exe')
driver.maximize_window()

driver.implicitly_wait(4)


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')

@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    driver.implicitly_wait(4)


@when('Click on search icon')
def click_search_icon(context):
    driver.wait = WebDriverWait(driver, 5)
    #context.driver.find_element(*SEARCH_SUBMIT).click()
    e = driver.wait.until(EC.element_to_be_clickable(*SEARCH_SUBMIT))
    e.click()



@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"
