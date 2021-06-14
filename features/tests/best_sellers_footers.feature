# Created by HDL32DA01 at 6/13/2021
Feature: Verify links on Amazon best sellers page
  # Enter feature description here

  Scenario: User sees links on Amazon best sellers page
    Given Open Amazon best sellers
    Then Verify best seller page 5 links are displayed