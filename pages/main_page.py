from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class MainPage(Page):
    SEARCH_BTN = (By.CSS_SELECTOR, '.modal__toggle-open.icon.icon-search')
    SEARCH_INPUT = (By.ID, 'Search-In-Modal')
    SEARCH_SUBMIT = (By.CSS_SELECTOR, '.search__button.field__button .icon.icon-search')

    def open_google(self):
        self.open_url()

    def input_search(self, search_word):
        self.find_element(*self.SEARCH_BTN).click()
        self.input_text(search_word, *self.SEARCH_INPUT)
        self.find_element(*self.SEARCH_SUBMIT).click()
        # sleep(4)
