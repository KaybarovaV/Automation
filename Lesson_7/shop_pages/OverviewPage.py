from selenium.webdriver.common.by import By
class OverviewPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/checkout-step-two.html')
        self._driver.maximize_window()
    def total_price(self):
        total = self._driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
        return total