from selenium.webdriver.common.by import By
class InventoryPage:
    """
    Этот класс описывает страницу с товарами, где можно выбрать элемент, добавить в корзину, почитать описание о товаре
    """
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/inventory.html')
        self._driver.maximize_window()
    def add_to_cart(self, item: str):
        """
        Нажать кнопку Add to cart элемента, введенного в параметр 
        """
        self._driver.find_element(By.CSS_SELECTOR, item).click()
    def click_to_cart(self):
        """
        Нажать кнопку shopping-cart-link (корзина)
        """
        self._driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
        