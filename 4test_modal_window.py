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


def test_modal():
    for driver_name in drivers:
        driver = driver_name
        driver.get("http://the-internet.herokuapp.com/entry_ad")
        path_window = '//*[@id="modal"]/div[2]/div[3]/p'
        search_window_button = (By.XPATH, path_window)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(search_window_button)).click()
        print("Система отработала")
        driver.close()
        driver.quit()


test_modal()
