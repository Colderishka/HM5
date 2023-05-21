from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/entry_ad")
path_window = '//*[@id="modal"]/div[2]/div[3]/p'
search_window_button = driver.find_element(By.XPATH, path_window)
sleep(3)
search_window_button.click()

sleep(5)
