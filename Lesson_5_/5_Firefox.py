from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()
# открыть страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# ввести в поле текст 1000
input = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
input.send_keys("1000")
sleep(2)

# очистить поле методом clear
input.clear()
sleep(2)

# ввести в это же поле текст 999
input.send_keys("999")

sleep(2)
driver.quit()