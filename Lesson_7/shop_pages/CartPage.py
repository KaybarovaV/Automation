from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/cart.html')
        self._driver.maximize_window()
    def checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()