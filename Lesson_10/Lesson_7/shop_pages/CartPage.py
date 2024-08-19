from selenium.webdriver.common.by import By
class CartPage:
    """
        Этот класс описывает страницу корзины.
    """
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/cart.html')
        self._driver.maximize_window()
    def checkout(self):
        """
        Нажатие на кнопку Checkout
        """
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()
