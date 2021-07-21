from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResults(Page):
    # SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    #SEARCH_RESULT = (By.ID, 'ap_email')
    SEARCH_RESULT = (By.CSS_SELECTOR, '#sc-active-cart h2')
    PRODUCT_RESULT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
    BOOKS_SUBAV = (By.CSS_SELECTOR, "#nav-subnav[data-category='books']")
    VIDEO_GAMES_SUBAV = (By.CSS_SELECTOR,"#nav-subnav[data-category='videogames']" )

    def click_first_product(self):
        self.click(*self.PRODUCT_RESULT)
    def verify_search_worked(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)
    def verify_books_department(self):
        self.wait_for_element_to_appear(*self.BOOKS_SUBAV)

    def verify_video_games(self):
        self.wait_for_element_to_appear(*self.VIDEO_GAMES_SUBAV)
    #def verify_search_worked(self):
    #    self.verify_text(*self.SEARCH_RESULT)