from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Shopping:
    def shop(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        # открыть страницу
        driver.get("https://www.saucedemo.com/")
        # авторизоваться как пользователь standard_user
        driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
        driver.find_element(By.CSS_SELECTOR, '#login-button').click()
        # добавить в корзину товары: Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie.
        driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
        # перейти в корзину
        driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
        # нажать checkout
        driver.find_element(By.CSS_SELECTOR, '#checkout').click()
        # заполнить форму своими данными (Вероника, Кайбарова, 655700)
        driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Вероника')
        driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Кайбарова')
        driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('655700')
        sleep(1)
        # нажать кнопку Continue
        driver.find_element(By.CSS_SELECTOR, '#continue').click()
        sleep(1)
        # прочитать со страницы итоговую стоимость (Total)
        txt = driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
        assert txt == 'Total: $58.29', 'Стоимость не равна $58.29'

        sleep(1)
        driver.quit()
        return True