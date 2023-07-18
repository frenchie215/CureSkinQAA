from selenium.webdriver.common.by import By
from pages.base_page import Page
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



SEARCH_FIELD = (By.ID, "Search-In-Modal")
# SEARCH_INPUT = (By.CSS_SELECTOR, 'input#Search-In-Modal.search__input.field__input') #q
SEARCH_ICON = (By.CSS_SELECTOR, "svg.icon.icon-search.modal__toggle-open")
SEARCH_RESULT = (By.CSS_SELECTOR, "#product-count.product-count__text")
CLOSE_POPUP = (By.CSS_SELECTOR, "div.popup-wrapper button.popup-close")


@given('Open main page')
def open_main(context):
    context.app.main_page.open_main()


@when('Click search button')
def click_search_icon(context):
    try:
        # Wait for the pop-up to appear
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located(CLOSE_POPUP))
    except TimeoutException:
        pass
    # Click the close button
    context.driver.find_element(*CLOSE_POPUP).click()

    # #able to click search btn
    # wait.until(EC.element_to_be_clickable(SEARCH_ICON))

    # # click search btn
    context.app.header.click_search()



@when('Input text {text}')
def input_search_word(context, text):
    # context.driver.find_element(*SEARCH_FIELD).send_keys(text)
    context.app.header.input_search_word(text)




@then('Verify the text {expected_result} is shown')
def verify_search_results(context, expected_result):
    context.app.search_results_page.verify_search_results(expected_result)
    # actual_result = context.driver.find_element(By.CSS_SELECTOR, "p#product-count.product-count__text").text
    # assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'

