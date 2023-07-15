from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.CSS_SELECTOR, 'input#Search-In-Modal.search__input.field__input') #q
SEARCH_SUBMIT = (By.CSS_SELECTOR, "button.search__button.focus-inset")
SEARCH_FIELD = (By.CSS_SELECTOR, "svg.icon.icon-search.modal__toggle-open")


@given('Open main page')
def open_cureskin(context):
    context.driver.get('https://shop.cureskin.com//')
    # context.app.main_page.function_name()


@when('Click search btn')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_FIELD).click()


@when('Input text {text}')
def input_search_word(context, text):
    context.driver.find_element(*SEARCH_FIELD).send_keys(text)


# @when('Search for {search_word} ')
# def input_search(context, search_word):
#     search = context.driver.find_element(*SEARCH_SUBMIT)
#     search.clear()
#     search.send_keys(search_word)


@then('Verify the results have SPF')
def verify_search_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'



@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'
