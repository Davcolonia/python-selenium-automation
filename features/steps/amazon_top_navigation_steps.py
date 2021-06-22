from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep, time


#SEARCH_INPUT = (By.NAME, 'q')
#SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Amazon')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.ID, 'nav-cart').click()

@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

@when('Click Sign In from popup')
def click_sign_in_btn(context):
    e = context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")))
    e.click()


@when('Search for coffee mug')
def search_for_product(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee mug', Keys.ENTER)

@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(
        By.XPATH, "//div[@data-component-type = 's-search-result']//a[.//span[@class='a-price']]").click()

@when('Click on the Add to cart button once')
def click_add_to_cart(context):
    context.driver.find_element(By.XPATH, "//span[@class='a-button-inner']").click()
    context.driver.find_element(By.ID, "add-to-cart-button").click()
    sleep(10)


@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    expected_count = int(expected_count)
    items_in_cart = context.driver.find_element(
        By.XPATH, "//*[@id='nav-cart-count']").text
    items_in_cart = int(items_in_cart)
    print('Items in cart:', items_in_cart)
    assert items_in_cart == expected_count, f'Expected {expected_count}, but got {items_in_cart}'

@then('Verify hamburger menu icon is visible')
def verify_ham_menu_visible(context):
    context.driver.find_element(By.ID, 'nav-hamburger-menu')

@then('Verify {expected_count} footer links are displayed')
def verify_footer_links_amount(context, expected_count):
    expected_count = int(expected_count)
    link_count = len(context.driver.find_elements(By.CSS_SELECTOR, ".navFooterDescItem a.nav_a"))
    assert link_count == expected_count, f'Expected {expected_count} links, but got {link_count}'

