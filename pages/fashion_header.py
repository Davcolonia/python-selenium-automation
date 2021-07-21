from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class FashionHeader(Page):
    NEW_ARRIVALS = (By.CSS_SELECTOR, "#nav-subnav a.nav-hasArrow[href*='/s/ref=']")
    WOMEN_FASHION = (By.CSS_SELECTOR, "a.mm-merch-panel[href*='/s?i=fashion-womens'] li")

    def hover_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_women_fashion_panel_present(self):
        self.wait_for_element_to_appear(*self.WOMEN_FASHION)
