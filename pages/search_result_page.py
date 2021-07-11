from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResults(Page):
    # SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    #SEARCH_RESULT = (By.ID, 'ap_email')
    SEARCH_RESULT = (By.CSS_SELECTOR, '#sc-active-cart h2')
    def verify_search_worked(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)
    #def verify_search_worked(self):
    #    self.verify_text(*self.SEARCH_RESULT)