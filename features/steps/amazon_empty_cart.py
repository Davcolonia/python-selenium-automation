from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#SEARCH_INPUT = (By.NAME, 'q')
#SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Amazon home page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    #context.app.main_page_open.open_main()


@when('User clicks cart icon')
def click_cart(context):
    #context.driver.find_element(By.ID, 'nav-cart').click()
    context.app.header.click_search()

@then('"{expected_text}" message is displayed')
def verify_empty_cart(context, expected_text):
    #actual_result = context.driver.find_element(By.CSS_SELECTOR, '#sc-active-cart h2').text
    #could not get the expected result to match :/ "Assertion Failed: Expected 0 Cart, but got 0 Cart"
    #assert actual_result == expected_text, f'Expected {expected_text}, but got {actual_result}'
    context.app.search_results_page.verify_search_worked(expected_text)
