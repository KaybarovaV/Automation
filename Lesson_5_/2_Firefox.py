from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

# открыть страницу
driver.get("http://uitestingplayground.com/dynamicid")

# нажать на синюю кнопку 3 раза
for i in range(3):
    click = driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
    click.click()

# проверить, что скрипт отработал
print("Скрипт успешно выполнен!")

sleep(2)
driver.quit()