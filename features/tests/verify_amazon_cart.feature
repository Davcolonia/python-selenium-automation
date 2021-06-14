# Created by HDL32DA01 at 6/6/2021
Feature: Test Scenarios for cart functionality

  Scenario: User clicks cart icon and verifies that Amazon cart is empty
    Given Open Amazon home page
    When User clicks cart icon
    Then "Your Amazon Cart is empty" message is displayed

    Scenario: User can add a product to the cart
      Given Open Amazon
      When Search for coffee mug
      And Click on the first product
      And Click on the Add to cart button once
      Then Verify cart has 1 item

     #   Scenario: User can add a product to the cart
     # Given Open Amazon
     # When Search for shoes
     # And Click on the first product
     # And Click on Size DD
     # And Click on 2nd size option
     # And Click on the Add to cart button
     # Then Verify cart has 1 item