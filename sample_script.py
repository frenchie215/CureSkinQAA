from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


#init driver



# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.wait = WebDriverWait(driver, 10) # start with driver.wait
# checks for condition to be not everyone 500ms (1/2 s)
# defined in the spot where we need it
# always foils with TimeoutException


#applied to all find element(s) functions
#100 ms = 0.1 s
# defined once
#not modifying the error / exception
driver.implicitly_wait(5) #check every 100 ms


# open the url
driver.get('https://www.google.com/')


# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Desk')

# wait for 4 sec
driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')), message='Search btn not clickable')


# click search
driver.find_element(By.NAME, 'btnK').click()


# verify search results
assert 'desk' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
