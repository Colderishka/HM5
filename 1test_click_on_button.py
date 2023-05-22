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


def test_click():
    for driver_name in drivers:
        driver = driver_name
        driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
        search_button_location = '[onclick="addElement()"]'
        search_button = driver.find_element(
            By.CSS_SELECTOR, search_button_location)
    for i in range(5):
        search_button.send_keys(Keys.RETURN)
        search_list = '[class="added-manually"]'
        search_list_for_print = driver.find_elements(
            By.CSS_SELECTOR, search_list)
        print(len(search_list_for_print))
    driver.close()
    driver.quit()


test_click()
