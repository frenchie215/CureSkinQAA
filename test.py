from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#uppercase for locators)
SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']")
# AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
# SEARCH_ICON = (By.ID, 'nav-search-submit-button')
PRODUCT_IMG = (By.XPATH, ".s-image[data-image-latency='s-product-image']")
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')

ORDERS_BTN = (By.ID, 'nav-orders')
# SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, "navFooterMoreOnAmazon a")
HEADER_LINKS = (By.CSS_SELECTOR, "#nav-xshop a.nav-a[data-csa-c-type='link']")
POPUP_SIGNIN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-signin-button")



@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input text coffee')
def input_search_word(context):
    context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys('coffee')

# #could also do below example if there are similar inputs but just different words
# # @when('Input text {search_word}')
# def input_search_word(context, search_word):
#     context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)


@when('Click on search button')
def click_search(context):
    # context.driver.find_element(*SEARCH_ICON).click()
    context.app.header.click_search()

@when('Click on button from SignIn popup')
def click_sign_in_popup_btn(context):
    context.driver.wait.until(EC.element_to_be_clickable(POPUP_SIGNIN_BTN)).click()
    #feel free to add error message if need to, for example:
    context.driver.wait.until(
        EC.element_to_be_clickable(POPUP_SIGNIN_BTN),
        message='Sign in btn not clickable'
    ).click()


@when('Wait for {sec} sec')
def wait_for_sec(context, sec):
    # '8' => 8
    sleep(int(sec)


@then('Verify sign in popup shown')
def verify_sign_in_popup_visible(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_BTN),
        message='Sign in btn not clickable'
    )


@then('Verify Sign In popup disappears')
def verify_sign_in_popup_not_visible(context):
    context.driver.wait.until(
        EC.invisibility_of_element_located(SIGN_IN_BTN),
        message='Sign in did not disappear'
    )



@then('Verify that text "coffee" is shown')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
   # Webelement1, webelement2, webelement3
    print(all_products)
#for loop
    for product in all_products:
        print(product)
        assert product.find_element(*PRODUCT_IMG).is_displayed(), f'Product image is missing' #f = error #.is_displayed() not required
        print(product.find_element(*PRODUCT_TITLE).text)
        assert product.find_element(*PRODUCT_TITLE).text, 'Product title is missing'

        # you can also do:
@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    print(f'Amount of products found: {lens(all_products)}')
    print(all_products)

    for product in all_products:
    print(product)
    assert product.find_element(*PRODUCT_IMG).is_displayed(), 'Product image is missing'  # f = error #.is_displayed() not required
    product_title = product.find_element(*PRODUCT_TITLE).text
    assert product_title, 'Product title is missing'


@then('Verify Sign In page opens')
def verify_signin_opens(context):
    actual_text = context.driver.find_element(*SIGNIN_HEADER).text
    assert actual_text == 'Sign in', f'Expected Sign in header but got {actual_text}'
    # verify email field present
    context.driver.find_element(*EMAIL)
    context.driver.wait.until(EC.url_contains('http://www.amazon.com/ap/signin'))


then@



# good to use for search results, registrations(username and password)
# To make scenarios that are all similar, just use scenario outlines
# Scenario Outline: User can search for coffee on Amazon
#     Given Open Amazon page
#     When Input text <search_word>
#     And Click on search button
#     Then Verify that text <search_result> is shown
#     Examples:
#     |search_word  |search_result  |
#     |coffee       |"coffee"       |
#     |table        |"table"        |
#     |mug          |"mug"          |