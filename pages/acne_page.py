from selenium.webdriver.common.by import By
from pages.base_page import Page


class AcnePage(Page):
    HEADER = (By.CSS_SELECTOR, '.collection-hero__title')

    def for_acne_shown(self):
        expected_text = 'For Acne'
        actual_text = self.find_element(*self.HEADER).text
        assert expected_text in actual_text, f'Expected {expected_text} to be in {actual_text}'
