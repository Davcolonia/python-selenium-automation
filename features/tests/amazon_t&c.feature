# Created by HDL32DA01 at 6/27/2021
Feature: Test for terms and conditions page
  # Enter feature description here


Scenario: User can open and close Amazon Privacy Notice
 Given Open Amazon T&C page
 When Store original window
 When Click on Amazon Privacy Notice link (*see image below)
 When Switch to the newly opened window
 Then Verify Amazon Privacy Notice page is opened
 When User can close new window and switch back to original
