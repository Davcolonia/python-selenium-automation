# Created by HDL32DA01 at 5/26/2021
Feature: Test Amazon search

  Scenario: User can search for a product
    Given Open Amazon page
    When Input Table in search field
    And Click on Amazon search icon
    Then Verify search worked for "Table"

    Scenario: User can add product to the cart
      Given Open Amazon page
      When Search for coffee
      And Click on the first product
      And Click on the Add to cart button once
      Then Verify cart has 1 item

    Scenario: Amazon footer has correct amount of links
      Given Open Amazon page
      Then Verify 48 footer links are displayed

  Scenario: User can select blouse colors
    Given Open Amazon product B07NF7J1SH page
    Then Verify user can click through colors

  Scenario: User can see deals under New Arrivals
    Given Open Amazon product B07NF7J1SH page
    When Mouse move over new arrivals
    Then Women fashion deals are shown

    Scenario: User can browse hoodie colors
      Given Open Amazon product B082YRMQLL page
      Then Verify user can click through colors

      Scenario: User can select and search in a department
        Given Open Amazon page
        When Select department by alias stripbooks
        And Search for Faust
        Then Verify books department is selected

    Scenario: User can select and search in games department
        Given Open Amazon page
        When Select department by alias videogames
        And Search for switch
        Then Verify video games department is selected