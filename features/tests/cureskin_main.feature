# Created by thebe at 12/13/2022
Feature: Tests for CureSkin main page

  Scenario: User can shop by concern
    Given Open main page
    When Click to Shop by Concern - Select Acne
    Then For Acne is shown

