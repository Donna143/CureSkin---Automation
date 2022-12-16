from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    REMOVE = (By.CSS_SELECTOR, '.icon.icon-remove')
    CART_EMPTY = (By.CSS_SELECTOR, '.cart__empty-text')

    def delete_product(self):
        self.find_element(*self.REMOVE).click()

    def cart_empty(self):
        expected_text = 'Your cart is empty'
        self.wait_for_element_disappear(*self.REMOVE)
        self.verify_partial_text(expected_text, *self.CART_EMPTY)




