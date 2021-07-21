# Created by HDL32DA01 at 7/18/2021
Feature: Language selection tests
  # Enter feature description here

  Scenario: User can see Spanish Language option
    Given Open Amazon page
    When Move mouse over flag icon
    Then Spanish language selection is visible