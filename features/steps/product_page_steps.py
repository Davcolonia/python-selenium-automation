from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')

# @when('Click on the Add to cart button')
# def click_add_to_cart_size(context):
#     if len(context.find_element(By.ID, 'native-dropdown_selected_size_name')) == 1:
#         context.driver.find_element(By.ID, 'native-dropdown_selected_size_name').click()
#         context.driver.find_element(By.ID, 'size_name_2')
#     context.driver.find_element(By.ID, 'add-to-cart-button').click()
#     sleep(5)

# @then('Verify user can click through colors')
# def verify_can_loop_thru_colors(context):
#     expected_colors = ["Dark Navy", "Dusty Rose", "Black"]
#     color_web_elements = context.driver.find_elements(By.CSS_SELECTOR, "#variation_color_name li")

    @then('Verify user can click through colors')
    def verify_can_loop_thru_colors(context):
        colors = ["Black Heather/Egret Logo", "Mood Indigo Heather", "Vintage Indigo/Egret Logo", "Wolf Grey Heather"]
        color_elements = context.driver.find_elements(By.CSS_SELECTOR, "#variation_color_name li")

        for i in range(len(color_elements)):
          color_elements[i].click()
          actual_text = context.driver.find_element(By.CSS_SELECTOR, "#variation_color_name span.selection").text
          assert actual_text == colors[i], f'Error, color is {actual_text}, but expected {colors[i]}'

    # for i in range(len(color_elements)):
    #     color_elements[i].click()
    #     actual_text = context.driver.find_element(By.CSS_SELECTOR, '#variation_color_name span.selection').text
    #     assert actual_text == expected_colors[i], f'Error, color is {actual_text}, but expected {expected_colors[i]}'
