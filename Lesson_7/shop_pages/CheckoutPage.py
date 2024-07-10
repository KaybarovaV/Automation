from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/checkout-step-one.html')
        self._driver.maximize_window()
    def input_firstname(self, firstname):
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(firstname)
    def input_lastname(self, lastname):
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(lastname)
    def input_postalcode(self, postalcode):
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postalcode)
    def click_continue(self):
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()