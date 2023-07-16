from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.keys import Keys



class Header(Page):
    SEARCH_FIELD = (By.ID, "Search-In-Modal")
    SEARCH_ICON = (By.CSS_SELECTOR, "svg.icon.icon-search.modal__toggle-open")
    CLOSE_POPUP = (By.CSS_SELECTOR, "div.popup-wrapper button.popup-close")

    def input_search_word(self, text):
        search_field = self.driver.find_element(*self.SEARCH_FIELD)
        search_field.send_keys(text)
        search_field.send_keys(Keys.ENTER)

        # self.input_text(text, *self.SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def close_button(self):
        self.click(*self.CLOSE_POPUP)





