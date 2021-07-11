import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep


#SEARCH_INPUT = (By.NAME, 'q')
#SEARCH_SUBMIT = (By.NAME, 'btnK')
TOP_LINKS = (By.CSS_SELECTOR, '#zg_tabs a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text_wrapper')

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

@then('User can click through top links and verify correct page opens')
def click_thru_top(context):
    top_links = context.driver.find_elements(*TOP_LINKS)

    for x in range(len(top_links)):
        link = context.driver.find_elements(*TOP_LINKS)[x]
        link_text = link.text
        link.click()

        header_text = context.driver.find_elements(*HEADER).text
        assert link_text in header_text, f'Expected {link_text} not in {header_text}'