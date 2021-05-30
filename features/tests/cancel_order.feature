# Created by HDL32DA01 at 5/30/2021
Feature: Test Scenarios for cancel order functionality

  Scenario: User can cancel their order for a product
    Given Open Amazon help page
    When Input cancel order into search help library field
    And Click Enter
    Then 'Cancel items or orders' text is shown