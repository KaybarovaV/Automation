from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(30)

# открыть страницу
driver.get("http://uitestingplayground.com/textinput")

# указать в поле ввода текст SkyPro
driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

# нажать на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

# получить текст кнопки и вывести в консоль
txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(txt)