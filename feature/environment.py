from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """

    # Get the path to the ChromeDriver executable
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # context.driver = webdriver.Firefox()
    # context.driver = webdriver.Safari()

    #### HEADLESS MODE ####
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    options = Options() #
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    context.driver = webdriver.Chrome(
        options=options,
        service=service
    )

    #### BROWSERSTACK ####
    # desired_cap = {
    #     'browser': 'Firefox',
    #     'os_version': '11',
    #     'os': 'Windows',
    #     'name': test_name
    # }
    # bs_user = ''
    # bs_key = ''
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario:', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step:', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed:', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
