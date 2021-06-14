from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep


# @when('Click on the Add to cart button')
# def click_add_to_cart_size(context):
#     if len(context.find_element(By.ID, 'native-dropdown_selected_size_name')) == 1:
#         context.driver.find_element(By.ID, 'native-dropdown_selected_size_name').click()
#         context.driver.find_element(By.ID, 'size_name_2')
#     context.driver.find_element(By.ID, 'add-to-cart-button').click()
#     sleep(5)
