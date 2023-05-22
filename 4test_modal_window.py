from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as GeckoService

driver = webdriver.Firefox(
    service=GeckoService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/entry_ad")
path_window = '//*[@id="modal"]/div[2]/div[3]/p'
search_window_button = driver.find_element(By.XPATH, path_window)
search_window_button.click()

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/entry_ad")
path_window = '//*[@id="modal"]/div[2]/div[3]/p'
search_window_button = driver.find_element(By.XPATH, path_window)
search_window_button.click()