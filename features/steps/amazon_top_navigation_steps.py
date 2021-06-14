from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


#SEARCH_INPUT = (By.NAME, 'q')
#SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Amazon')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.ID, 'nav-cart').click()

@when('Search for coffee mug')
def search_for_product(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee mug', Keys.ENTER)

@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(
        By.XPATH, "//div[@data-component-type = 's-search-result']//a[.//span[@class='a-price']]").click()

@when('Click on the Add to cart button once')
def click_add_to_cart(context):
    sleep(4)
    context.driver.find_element(By.XPATH, "//span[@class='a-button-inner']").click()


@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    #expected_count = int(expected_count) @Lana tried various things here but still recieved: Assertion Failed: Expected 1, but got 0
    items_in_cart = context.driver.find_element(
        By.XPATH, "//div[@id='nav-cart-count-container']//span[@id='nav-cart-count']").text
    print('Items in cart: ', items_in_cart)
    assert items_in_cart == expected_count, f'Expected {expected_count}, but got {items_in_cart}'

@then('Verify hamburger menu icon is visible')
def verify_ham_menu_visible(context):
    context.driver.find_element(By.ID, 'nav-hamburger-menu')

@then('Verify {expected_count} footer links are displayed')
def verify_footer_links_amount(context, expected_count):
    expected_count = int(expected_count)
    link_count = len(context.driver.find_elements(By.CSS_SELECTOR, ".navFooterDescItem a.nav_a"))
    assert link_count == expected_count, f'Expected {expected_count} links, but got {link_count}'