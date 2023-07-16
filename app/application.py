from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)




# app = Application('driver')
# app.main_page.open_main()
# app.header.click_search()
