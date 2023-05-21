
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


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")
path_to_field_login = "#username"
search_field = driver.find_element(By.CSS_SELECTOR, path_to_field_login)
search_field.send_keys("tomsmith")
path_to_field_password = "#password"
sleep(2)
search_field = driver.find_element(By.CSS_SELECTOR, path_to_field_password)
search_field.send_keys("SuperSecretPassword!")
sleep(2)
path_to_login = "[class='radius']"
search_field = driver.find_element(By.CSS_SELECTOR, path_to_login)
search_field.send_keys(Keys.RETURN)

sleep(10)