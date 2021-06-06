from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from time import sleep


#SEARCH_INPUT = (By.NAME, 'q')
#SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Amazon help page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input cancel order into search help library field and Click Enter')
def search_amazon_help(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys('Cancel order', Keys.ENTER)

#@when('Click Enter')
#def click_search(context):
#    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Verify Cancel items or Orders text is shown')
def verify_found_results_text_help_page(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='help-content']//h1").text
    expected_result = "Cancel Items or Orders"
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
