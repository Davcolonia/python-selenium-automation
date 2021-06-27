from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

@when('Store original window')
def store_window(context):
    context.original_window = context.driver.current_window_handle

@when('Click on the dog image')
def click_img(context):
    context.driver.find_element(By.CSS_SELECTOR, "img#d").click()

@when('Switch to new window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)

    win_handles = context.driver.window_handles
    context.driver.switch_to.window(win_handles[0])

@when('Return to original window')
def switch_to_original_window(context):
    context.driver.switch_to.window(context.original_window)

@then('Verify Amazon Blog url')
def verify_blog_url(context):
    assert 'https://www.aboutamazon.com/' in context.driver.current_url, \
        f'Url https://www.aboutamazon.com/ not in {context.driver.current_url}'

@then('Verify Amazon url')
def verify_blog_url(context):
    assert 'https://www.amazon.com/' in context.driver.current_url, \
        f'Url https://www.amazon.com/ not in {context.driver.current_url}'

@then('Close new window')
def close_window(context):
    context.driver.close()