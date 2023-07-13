from pages.search_results_page import SearchResults
from pages.main_page import MainPage
from pages.search_details_page import SearchDetails
from pages.shopping_page import ShoppingPage


class Application:

def     init    (self, driver):
    self.driver = driver
    self.search_results = SearchResults(driver)
    self.main_page = MainPage(driver)
    self.search_details = SearchDetails(driver)
    self.shopping_page = ShoppingPage(driver)