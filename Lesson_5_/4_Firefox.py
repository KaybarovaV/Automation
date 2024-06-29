from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

# открыть страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(2)

# нажать кнопку закрытия
click = driver.find_element(By.XPATH, "//p[text()='Close']")
click.click()

sleep(2)
driver.quit()