from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# открыть страницу
driver.get("http://uitestingplayground.com/classattr")

# три раза нажать на синюю кнопку
for i in range(3):
    click = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), 'btn-primary')]")
    click.click()
    sleep(2)
    alert = driver.switch_to.alert
    alert.accept()
    sleep(2)

driver.quit()