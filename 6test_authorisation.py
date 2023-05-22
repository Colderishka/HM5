from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as GeckoService

drivers = [
    webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
    webdriver.Firefox(service=GeckoService(GeckoDriverManager().install()))
]


def test_authorisation():
    for driver_name in drivers:
        driver = driver_name
        driver.get("http://the-internet.herokuapp.com/login")
        path_to_field_login = "#username"
        search_field = driver.find_element(
            By.CSS_SELECTOR, path_to_field_login)
        search_field.send_keys("tomsmith")
        path_to_field_password = "#password"
        search_field = driver.find_element(
            By.CSS_SELECTOR, path_to_field_password)
        search_field.send_keys("SuperSecretPassword!")
        path_to_login = "[class='radius']"
        search_field = driver.find_element(By.CSS_SELECTOR, path_to_login)
        search_field.send_keys(Keys.RETURN)
        driver.close()
        driver.quit()


test_authorisation()
