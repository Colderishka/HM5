
# 1. Откройте страницу 
# [http://the-internet.herokuapp.com/login](http://the-internet.herokuapp.com/login).
# 2. В поле username введите значение `tomsmith`.
# 3. В поле password введите значение `SuperSecretPassword!`.
# # 4. Нажмите кнопку `Login`.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as GeckoService

driver = webdriver.Firefox(
    service=GeckoService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")
path_to_field_login = "#username"
search_field = driver.find_element(By.CSS_SELECTOR, path_to_field_login)
search_field.send_keys("tomsmith")
path_to_field_password = "#password"
search_field = driver.find_element(By.CSS_SELECTOR, path_to_field_password)
search_field.send_keys("SuperSecretPassword!")
path_to_login = "[class='radius']"
search_field = driver.find_element(By.CSS_SELECTOR, path_to_login)
search_field.send_keys(Keys.RETURN)

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")
path_to_field_login = "#username"
search_field = driver.find_element(By.CSS_SELECTOR, path_to_field_login)
search_field.send_keys("tomsmith")
path_to_field_password = "#password"
search_field = driver.find_element(By.CSS_SELECTOR, path_to_field_password)
search_field.send_keys("SuperSecretPassword!")
path_to_login = "[class='radius']"
search_field = driver.find_element(By.CSS_SELECTOR, path_to_login)
search_field.send_keys(Keys.RETURN)
