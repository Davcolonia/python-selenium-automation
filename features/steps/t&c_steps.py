from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

@given('Open Amazon T&C page')
def open_terms_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 ')

@when('Click on Amazon Privacy Notice link (*see image below)')
def click_privacy_notice(context):
    context.driver.find_elements(By.XPATH, "//a[@href='https://amazon.com/privacy']")

@when('Switch to the newly opened window')
def switch_to_newly_open_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    win_handles = context.driver.window_handles
    # new_window = context.driver.window_handles
    context.driver.switch_to.window(win_handles[0])

@when('User can close new window and switch back to original')
def switch_to_original_window(context):
    context.driver.switch_to.window(context.original_window)

@then('Verify Amazon Privacy Notice page is opened')
def verify_blog_url(context):
    assert 'https://www.amazon.com/gp/help/customer' in context.driver.current_url, \
        f'Url https://www.amazon.com/gp/help/customer not in {context.driver.current_url}'

    sleep(1)


