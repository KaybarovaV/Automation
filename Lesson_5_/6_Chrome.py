from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# открыть страницу
driver.get("http://the-internet.herokuapp.com/login")

# в поле username ввести значение tomsmith
input_username = driver.find_element(By.CSS_SELECTOR, '#username')
input_username.send_keys("tomsmith")
sleep(2)

# в поле password введите значение SuperSecretPassword!
input_password = driver.find_element(By.CSS_SELECTOR, '#password')
input_password.send_keys("SuperSecretPassword!")
sleep(2)

# нажать кнопку Login
click = driver.find_element(By.CSS_SELECTOR, ".radius")
click.click()

sleep(2)
driver.quit()