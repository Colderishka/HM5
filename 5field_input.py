from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/inputs")
path_to_field = "[type='number']"
search_field = driver.find_element(By.CSS_SELECTOR, path_to_field)
search_field.send_keys("100")
sleep(2)
delite_field = driver.find_element(By.CSS_SELECTOR, path_to_field).clear()
sleep(2)
search_field.send_keys("999")

sleep(10)
