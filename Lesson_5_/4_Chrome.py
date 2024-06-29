from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# открыть страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(2)

# нажать кнопку закрытия
click = driver.find_element(By.XPATH, "//p[text()='Close']")
click.click()

sleep(2)
driver.quit()