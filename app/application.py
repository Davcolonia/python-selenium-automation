from pages.header import Header
from pages.main_page import Main
from pages.product_page import ProductPage
from pages.search_result_page import SearchResults
from pages.fashion_header import FashionHeader

class Application():
    def __init__(self, driver):
        self.driver = driver
        self.main_page = Main(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResults(self.driver)
        self.product_page = ProductPage(self.driver)
        self.fashion_header = FashionHeader(self.driver)