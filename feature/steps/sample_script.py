from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


#applied to all find element(s) functions
#100 ms = 0.1 s
# defined once
#not modifying the error / exception
driver.implicitly_wait(5)


# start with driver.wat
# checks for condition to be not everyone 500ms (1/2 s)
# defined in the spot where we need it
# always foils with TimeoutException
driver.wait = WebDriverWait(driver, 5)


# open the url
driver.get('https://www.google.com/')


# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Desk')

# wait for 4 sec
# sleep(4)
google_search_btn = (By.NAME, 'q')
driver.wait.until(EC.element_to_be_clickable(google_search_btn), message='Google search btn not clickable')


# click search button
driver.find_element(*google_search_btn).click()


# verify search results
assert 'desk' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
