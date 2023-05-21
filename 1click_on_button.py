from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
search_button_location = '[onclick="addElement()"]'
search_button = driver.find_element(By.CSS_SELECTOR, search_button_location)
for i in range(5):
    search_button.send_keys(Keys.RETURN)

search_list = '[class="added-manually"]'
search_list_for_print = driver.find_elements(By.CSS_SELECTOR, search_list)
print(len(search_list_for_print))
sleep(10)
