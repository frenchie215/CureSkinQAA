from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'SPF') #q
SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open main page')
def open_google(context):
    context.driver.get('https://www.shop.cureskin/')


@when('Click search')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()



@when('Search for {search_word} ')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)


@then('Verify the results have SPF')
def verify_search_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'



@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'
