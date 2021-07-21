from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep, time


#SEARCH_INPUT = (By.NAME, 'q')
#SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()

@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.ID, 'nav-cart').click()

@when('Click Orders')
def click_orders(context):
    # orders_link = context.driver.find_element(By.ID, 'nav-orders')
    # print(orders_link)
    # context.driver.refresh()
    # orders_link = context.driver.find_element(By.ID, 'nav-orders')
    # print(orders_link)
    # orders_link.click()
    context.app.header.click_search()

@when('Click Sign In from popup')
def click_sign_in_btn(context):
    e = context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")))
    e.click()

@when('Input {search_word} in search field')
def search_amazon(context, search_word):
    context.app.header.input_search(search_word)

@when('Click on Amazon search icon')
def click_search(context):
    context.app.header.click_search()

#@when('Search for coffee mug')
#def search_for_product(context):
#    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee mug', Keys.ENTER)

@when('Search for {search_word}')
def search_for_product(context, search_word):
    context.app.header.input_search_word(search_word)
    context.app.header.click_search()

@when('Click on the first product')
def click_first_product(context):
    # context.driver.find_element(
     #   By.XPATH, "//div[@data-component-type = 's-search-result']//a[.//span[@class='a-price']]").click()
    context.app.search_results_page.click_first_product()

@when('Move mouse over flag icon')
def hover_flag_icon(context):
    context.app.header.hover_flag_icon()
    sleep(10)

@when('Select department by alias {alias}')
def select_department(context, alias):
    context.app.header.select_department(alias)

@when("Mouse move over new arrivals")
def move_mouse(context):
    context.app.fashion_header.hover_new_arrivals()

@when('Click on the Add to cart button once')
def click_add_to_cart(context):
    context.driver.find_element(By.XPATH, "//span[@class='a-button-inner']").click()
    context.driver.find_element(By.ID, "add-to-cart-button").click()
    sleep(10)

#
# @then('Verify cart has {expected_count} item')
# def verify_cart_count(context, expected_count):
#     expected_count = int(expected_count)
#     items_in_cart = context.driver.find_element(
#         By.XPATH, "//*[@id='nav-cart-count']").text
#     items_in_cart = int(items_in_cart)
#     print('Items in cart:', items_in_cart)
#     assert items_in_cart == expected_count, f'Expected {expected_count}, but got {items_in_cart}'

@then('Verify hamburger menu icon is visible')
def verify_ham_menu_visible(context):
    context.driver.find_element(By.ID, 'nav-hamburger-menu')

@then('Verify {expected_count} footer links are displayed')
def verify_footer_links_amount(context, expected_count):
    expected_count = int(expected_count)
    link_count = len(context.driver.find_elements(By.CSS_SELECTOR, ".navFooterDescItem a.nav_a"))
    assert link_count == expected_count, f'Expected {expected_count} links, but got {link_count}'

@then('Verify Sign in popup is clickable')
def verify_signin_popup_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")))

@when('Wait for {sec_count} sec')
def sleep_sec(context, sec_count):
    sleep(int(sec_count))

@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    context.app.header.verify_cart_count(expected_count)

@then('Verify sign in popup disappears')
def verify_signin_popup_disappears(context):
    # context.driver.wait.until(condition == True)
    context.driver.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")))
    # context.driver.wait.until_not(condition == False)
    # context.driver.wait.until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")))

@then('Spanish language selection is visible')
def verify_spanish_lang_present(context):
    context.app.header.verify_spanish_lang_present()

@then('Verify Sign In page opened')
def verify_signin_opened(context):
    context.app.search_results_page.verify_search_worked()
    #context.driver.find_element(By.ID, 'ap_email')
    #assert 'https://www.amazon.com/ap/signin' in context.driver.current_url, f'Wrong url {context.driver.current_url}'

@then('Verify books department is selected')
def verify_books_department(context):
    context.app.search_results_page.verify_books_department()

@then('Verify video games department is selected')
def verify_books_department(context):
    context.app.search_results_page.verify_video_games()

@then("Women fashion deals are shown")
def verify_womens_fashion(context):
    context.app.fashion_header.verify_women_fashion_panel_present()

