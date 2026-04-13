Feature: E2E Checkout Flow

  Scenario: Successful purchase of a single item
    Given the user is logged into the system
    When I select the product "Sauce Labs Backpack"
    And I complete the checkout with shipping details
    Then the order should be processed successfully
    And the system should display the message "Thank you for your order"

  Scenario: Remove an item from the cart successfully
    Given the user is logged into the system
    When I select the product "Sauce Labs Backpack"
    And I remove the product from the cart
    Then the cart badge should be empty
