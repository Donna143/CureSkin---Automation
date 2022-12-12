from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT = (By.ID, 'MainContent')

    def no_search_results(self):
        expected_text = 'No results found'
        actual_text = self.find_element(*self.SEARCH_RESULT).text
        assert expected_text in actual_text, f'Expected {expected_text} to be in {actual_text}'
