from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, "#product-count.product-count__text")
    SEARCH_TEXT = (By.ID, 'ProductCount')  # q
    SEARCH_ICON = (By.CSS_SELECTOR, "svg.icon.icon-search.modal__toggle-open")
    SEARCH_FIELD = (By.ID, "Search-In-Modal")


    def verify_search_results(self, expected_text):
        search_text_word = self.driver.find_element(*self.SEARCH_TEXT)
        actual_text = search_text_word.text
        assert expected_text == actual_text, f"Expected search result text {expected_text}', but got {actual_text}'"
        self.verify_text(expected_text, *self.SEARCH_RESULT)


    def click_search(self):
        self.click(self.SEARCH_ICON)