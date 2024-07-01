from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(20)

# открыть страницу
driver.get("http://uitestingplayground.com/ajax")

# Нажать на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# получить текст из зеленой плашки
content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

# вывести текст в консоль
print(txt)

driver.quit()