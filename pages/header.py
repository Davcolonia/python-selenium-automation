from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    # SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    # SEARCH_ICON = (By.ID, 'nav-orders')
    SEARCH_ICON = (By.ID, 'nav-cart')
    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

