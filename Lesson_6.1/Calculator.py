from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Calculator:
    def calculator(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        # открыть страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        # в поле ввода по локатору #delay ввести значение 45
        driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        sleep(0.1)
        driver.find_element(By.CSS_SELECTOR, '#delay').send_keys('45')
        sleep(0.1)
        # нажать на кнопки: 7, +, 8, =
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        sleep(0.1)
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        sleep(0.1)
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        sleep(0.1)
        driver.find_element(By.XPATH, "//span[text()='=']").click()
        # проверить, что в окне отобразится результат 15 через 45 секунд
        sleep(47)
        result = driver.find_element(By.CSS_SELECTOR, '[class="screen"')
        assert result.text == '15', "Результат не равен 15"
        sleep(2)
        driver.quit()
        return True