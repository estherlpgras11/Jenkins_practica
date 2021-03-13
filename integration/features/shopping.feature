Feature: shopping ACME stuff
  
  Background: go to main site
    Given We are in the main site
 
  Scenario: count number of items
    Then 3 items must be displayed

  Scenario Outline: list current items
    Then "<item>" item must be displayed

    Examples: Items
        | item     | 
        | cohete   |
        | dinamita |
        | yunque   |
