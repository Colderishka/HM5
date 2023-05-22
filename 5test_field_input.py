from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as GeckoService

driver = webdriver.Firefox(
    service=GeckoService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/inputs")
path_to_field = "[type='number']"
search_field = driver.find_element(By.CSS_SELECTOR, path_to_field)
search_field.send_keys("100")
delite_field = driver.find_element(By.CSS_SELECTOR, path_to_field).clear()
search_field.send_keys("999")


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/inputs")
path_to_field = "[type='number']"
search_field = driver.find_element(By.CSS_SELECTOR, path_to_field)
search_field.send_keys("100")
delite_field = driver.find_element(By.CSS_SELECTOR, path_to_field).clear()
search_field.send_keys("999")
