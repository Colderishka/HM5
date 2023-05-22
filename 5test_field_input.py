from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as GeckoService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

drivers = [
    webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
    webdriver.Firefox(service=GeckoService(GeckoDriverManager().install()))
]


def test_field():
    for driver_name in drivers:
        driver = driver_name
        driver.get("http://the-internet.herokuapp.com/inputs")
        path_to_field = "[type='number']"
        search_field = driver.find_element(By.CSS_SELECTOR, path_to_field)
        search_field.send_keys("100")
        delite_field = driver.find_element(
            By.CSS_SELECTOR, path_to_field).clear()
        search_field.send_keys("999")
        print("система отработала")
        driver.close()
        driver.quit()


test_field()
