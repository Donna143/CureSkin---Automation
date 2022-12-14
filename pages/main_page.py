from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(Page):
    SEARCH_BTN = (By.CSS_SELECTOR, '.modal__toggle-open.icon.icon-search')
    SEARCH_INPUT = (By.ID, 'Search-In-Modal')
    SEARCH_SUBMIT = (By.CSS_SELECTOR, '.search__button.field__button .icon.icon-search')
    SHOP_CONCERN = (By.ID, 'Details-HeaderMenu-1')
    SHOP_CONCERN_MOBILE = (By.ID, 'Details-menu-drawer-menu-item-1')
    CATEGORY_ACNE = (By.XPATH, "//ul[@id='HeaderMenu-MenuList-1']//a[contains(text(), 'Acne')]")
    CATEGORY_ACNE_MOBILE = (By.XPATH, "//div[@id='link-Shop by Concern']//a[contains(text(), 'Acne')]")
    HAMBURGER = (By.ID, 'Details-menu-drawer-container')

    def open_google(self):
        self.open_url()

    def input_search(self, search_word):
        self.find_element(*self.SEARCH_BTN).click()
        self.input_text(search_word, *self.SEARCH_INPUT)
        self.find_element(*self.SEARCH_SUBMIT).click()

    def click_hamburger(self):
        self.find_element(*self.HAMBURGER).click()

    def click_concern_acne(self):
        concern = self.find_element(*self.SHOP_CONCERN)
        category = self.find_element(*self.CATEGORY_ACNE)
        actions = ActionChains(self.driver)
        actions.click(concern)
        actions.click(category)
        actions.perform()

    def mobile_click_concern_acne(self):
        concern = self.find_element(*self.SHOP_CONCERN_MOBILE)
        category = self.find_element(*self.CATEGORY_ACNE_MOBILE)
        actions = ActionChains(self.driver)
        actions.click(concern)
        actions.click(category)
        actions.perform()

