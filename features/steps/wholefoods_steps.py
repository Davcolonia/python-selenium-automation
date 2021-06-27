from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

BEST_DEALS_ITEMS = (By.XPATH, "//li[@class='s-result-item' and .//span[contains(@class,'prime-price')]]/div")
PRODUCT_NAME = (By.CSS_SELECTOR, "span.wfm-sales-item-card__product-name")

@given('Open Amazon Wholefoods page')
def open_wholefoods_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')

@then('verify that Wholefoods products have regular prices and names')
def verify_best_deals(context):
    best_deals_items = context.driver.find_elements(*BEST_DEALS_ITEMS)
    for e in best_deals_items:
        assert 'Regular' in e.text, f'Expected Regualr  price not'
        product_name = e.find_element(*PRODUCT_NAME).text
        print(product_name)
        assert product_name, f'Product name is missing'