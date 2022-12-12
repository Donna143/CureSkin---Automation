# Created by thebe at 12/9/2022
Feature: Tests for CureSkin search

  Scenario: User can search for non-existing product
    Given Open main page
    When Search for sdvghsfhdsgfdshg
    Then No search results are shown

