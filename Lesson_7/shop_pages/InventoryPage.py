from selenium.webdriver.common.by import By
class InventoryPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/inventory.html')
        self._driver.maximize_window()
    def add_to_cart(self, item):
        self._driver.find_element(By.CSS_SELECTOR, item).click()
    def click_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()