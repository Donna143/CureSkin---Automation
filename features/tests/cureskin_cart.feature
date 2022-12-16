# Created by thebe at 12/13/2022
Feature: Tests for CureSkin Cart

  Scenario: User can checkout
    Given Open Product Detail page
    When Click to Buy it now
    Then User is taken to checkout page
#
  Scenario: Product can be deleted from cart
    Given Open Product Detail page
    When Click Add to cart
    And Open Cart page
    When Delete the product
    Then Cart is empty

