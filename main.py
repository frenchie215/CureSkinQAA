from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

ORDERS_BTN = (By.ID, 'nav-orders')
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, "navFooterMoreOnAmazon a")
HEADER_LINKS = (By.CSS_SELECTOR, "#nav-xshop a.nav-a[data-csa-c-type='link']")
POPUP_SIGNIN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-signin-button")

@given('Open Amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {search_query}')
def search_amazon(context, search_query):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_query)
    context.driver.find_element(*SEARCH_ICON).click()


@when('Input text {text}')
def input_search_word(context, text):
    context.driver.find_element(*SEARCH_FIELD).send_keys(text)


@when('Click on search button')
def click_search(context):
    context.driver.find_element(*SEARCH_ICON).click()



@when('Click Orders')
def click_orders(context):
    context.driver.find_element(*ORDERS_BTN).click()


@when('Verify Orders btn present')
def click_orders(context):
    context.driver.find_element(*ORDERS_BTN)

@when('Click on button from SignIn popup')
def click_sign_in_popup_btn(context):
    signin_btn = context.driver.wait.until(EC. element_to_be_clickable(POPUP_SIGNIN_BTN), message='Signin btn not clickable')
    signin_btn.click()

@then('Verify there are {expected_amount} links')
def verify_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    print('After conversion: => ', type(expected_amount))

    links_count = len(context.driver.find_element(*FOOTER_LINKS)) #36
    print(type(links_count))




@then('Verify hamburger menu icon present')
def verify_ham_menu_present(context):
    context.driver.find_element(*HAM_MENU)
    # print(element)


@then('Verify that footer has {expected_amount} links')
def verify_footer_link_count(context, expected_amount):
    print('Original Type: ', type(expected_amount))  # '42'
    expected_amount = int(expected_amount)
    print('Type after converting: ', type(expected_amount))  # => 42

    footer_links = context.driver.find_elements(*FOOTER_LINKS)
    print(footer_links)
    print('\nLink count: ', len(footer_links))
    # assert 42 == 42
    assert len(footer_links) == expected_amount, f'Expected {expected_amount} links, but got {len(footer_links)}'


@then('Verify that header has {expected_amount} links')
def verify_header_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    header_links = context.driver.find_elements(*HEADER_LINKS)
    assert len(header_links) == expected_amount, f'Expected {expected_amount} links but got {len(header_links)}'