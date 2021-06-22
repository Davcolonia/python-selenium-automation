# Created by HDL32DA01 at 6/20/2021
Feature: Tests for sign in page

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Orders
    Then Verify Sign in page opened

  Scenario: Sign in page can be opened Sign In popup
    Given Open Amazon page
    When Click Sign In from popup
    Then Verify Sign In page opened

