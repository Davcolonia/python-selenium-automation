# Created by HDL32DA01 at 5/26/2021
Feature: Test Amazon search

  Scenario: User can search for a product
    Given Open Amazon page
    When Input Table in search field
    And Click on Amazon search icon
    Then Verify search worked

    Scenario: Amazon footer has correct amount of links
      Given Open Amazon page
      Then Verify 48 footer links are displayed

  Scenario: User can select blouse colors
    Given Open Amazon product B07NF7J1SH page
    Then Verify user can click through colors

    Scenario: User can browse hoodie colors
      Given Open Amazon product B082YRMQLL page
      Then Verify user can click through colors