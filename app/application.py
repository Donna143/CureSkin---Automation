from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.acne_page import AcnePage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.acne_page = AcnePage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.cart_page = CartPage(self.driver)





