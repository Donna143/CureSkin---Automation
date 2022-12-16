from selenium.webdriver.common.by import By
from pages.base_page import Page


class CheckoutPage(Page):

    def verify_checkout(self):
        expected_title = "Checkout"
        actual_title = self.driver.title
        assert expected_title in actual_title, f'Expected {expected_title} to be in {actual_title}'


