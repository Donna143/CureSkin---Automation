from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductPage(Page):
    ADD_CART = (By.CSS_SELECTOR, "[name='add']")
    BUY_NOW = (By.CSS_SELECTOR, "button[data-testid='Checkout-button']")
    VIEW_CART = (By.CSS_SELECTOR, '.icon.icon-cart')

    def open_product(self, product):
        self.open_url(product)

    def click_buy_now(self):
        self.find_element(*self.BUY_NOW).click()

    def add_cart(self):
        self.find_element(*self.ADD_CART).click()

    def view_cart(self):
        self.find_element(*self.VIEW_CART).click()




