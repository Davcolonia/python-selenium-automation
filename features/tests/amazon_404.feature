# Created by HDL32DA01 at 6/27/2021
Feature: Tests for 404 page
  # Enter feature description here

  Scenario: 404 page takes to Amazon Blog
    Given Open Amazon product INVALID____B082YRMQLL page
    When Store original window
    When Click on the dog image
    When Switch to new window
    Then Verify Amazon Blog url
    Then Close new window
    When Return to original window
    Then Verify Amazon url