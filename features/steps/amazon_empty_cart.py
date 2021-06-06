from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#SEARCH_INPUT = (By.NAME, 'q')
#SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Amazon home page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('User clicks cart icon')
def click_cart(context):
    context.driver.find_element(By.ID,'nav-cart').click()

@then('Verify that Your Amazon Cart is empty')
def verify_empty_cart(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'a#nav-cart.nav-a.nav-a-2.nav-progressive-attribute').text
    #could not get the expected result to match :/ "Assertion Failed: Expected 0 Cart, but got 0 Cart"
    expected_result = '0 Cart'
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
