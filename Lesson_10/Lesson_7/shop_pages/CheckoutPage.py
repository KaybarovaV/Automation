from selenium.webdriver.common.by import By
class CheckoutPage:
    """
        Этот класс описывает страницу Checkout с информацией о пользователе.
        Здесь можно заполнить информацию о себе, состоящая из 3 значений (Имя, Фамилия, Индекс)
    """
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/checkout-step-one.html')
        self._driver.maximize_window()
    def input_firstname(self, firstname: str):
        """
        Ввод в поле firstname значения, введенного в параметр 
        """
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(firstname)
    def input_lastname(self, lastname: str):
        """
        Ввод в поле lastname значения, введенного в параметр 
        """
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(lastname)
    def input_postalcode(self, postalcode: int):
        """
        Ввод в поле postalcode значения, введенного в параметр 
        """
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postalcode)
    def click_continue(self):
        """
        Нажатие на кнопку Continue
        """
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click() 
