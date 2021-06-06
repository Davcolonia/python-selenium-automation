from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#SEARCH_INPUT = (By.NAME, 'q')
#SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input Table in search field')
def search_amazon(context):
    context.driver.find_element(By.ID,'twotabsearchtextbox').send_keys('Table')


@when('Click on Amazon search icon')
def click_search(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Verify Search Worked')
def verify_found_results_text(context):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    expected_result = '"Table"'
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
