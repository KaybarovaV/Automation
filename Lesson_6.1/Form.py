from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class filling:
    def filling(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        # открыть страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        # заполнить форму
        driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys('Иван')
        driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys('Петров')
        driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys('Ленина, 55-3')
        driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys('test@skypro.com')
        driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys('+7985899998787')
        driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys('Москва')
        driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys('Россия')
        driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys('QA')
        driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys('SkyPro')
        # нажать кнопку submit
        driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        # проверить, что поле Zip code подсвечено красным
        zip_code_element = driver.find_element(By.CSS_SELECTOR, '#zip-code')
        assert "alert py-2 alert-danger" in zip_code_element.get_attribute("class"), "Поле Zip code не подсвечено красным"
        sleep(2)
        driver.quit()
        return True