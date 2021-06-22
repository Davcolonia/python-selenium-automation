import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep


#SEARCH_INPUT = (By.NAME, 'q')
#SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Amazon best sellers')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b')
    time.sleep(5)

@then('Verify best seller page {expected_links} links are displayed')
def verify_footer_links_amount(context, expected_links):
    expected_links = int(expected_links)
    link_count = len(context.driver.find_elements(By.XPATH, "//*[@id='zg_tabs']/ul/li/div/a"))
    print(link_count)
    assert link_count == expected_links, f'Expected {expected_links} links, but got {link_count}'
