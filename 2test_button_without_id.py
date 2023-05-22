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


def test_button():
    for driver_name in drivers:
        driver = driver_name
        driver.get("http://uitestingplayground.com/dynamicid")
        path_to_button = '[class="btn btn-primary"]'
        search_blue_button = driver.find_element(
            By.CSS_SELECTOR, path_to_button)
        search_blue_button.send_keys(Keys.RETURN)
        print("система отработала")
        driver.close()
        driver.quit()


test_button()
