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
