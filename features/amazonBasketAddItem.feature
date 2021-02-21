# Created by ianr at 20/02/2021
Feature: As a user, I want to add an item I like, so that I can purchase it later on.

  Scenario: 1. Add initial item
    Given the users basket has "0" items in it
    When the user adds the item to the basket
    Then the users basket has "1" items in it

  Scenario: 2. Add more items
    Given the users basket has at least "1" item
    When the user adds another item to the basket
    Then the users basket has "1" more item in it

  Scenario: 3. Add item multiple times
    Given the users basket has at least "1" item in it
    When the user adds more than "1" item to the basket
    Then the users basket has more than "1" item in it
    #Then teardown browser
