from selenium.webdriver.common.by import By
class MainPage:
    """
    Этот класс описывает страницу логинации пользователя. Здесь можно ввести два значения (username, password)
    """
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')
        self._driver.maximize_window()
    def login(self, username: str, password: str):
        """
        Ввод в поле  username и password значений, введенных в параметр и нажатие на кнопку Login
        """
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(username)
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()        
