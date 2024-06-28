from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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