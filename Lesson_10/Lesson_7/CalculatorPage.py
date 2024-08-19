from selenium.webdriver.common.by import By
class CalculatorPage:
    """
    Этот класс описывает страницу калькулятора, где можно использовать функцию калькулятора с установленным таймером ожидания ответа
    """
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._driver.maximize_window()
    def input_timer(self, timer: int):
        """
        Очистить поле 'calculator waits' и ввести туда значение, введенное в параметр
        """
        self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(timer)
    def click7(self):
        """
        Нажать кнопку '7'
        """
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
    def click_add(self):
        """
        Нажать кнопку '+'
        """
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
    def click8(self):
        """
        Нажать кнопку '8'
        """
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
    def click_equals(self):
        """
        Нажать кнопку '='
        """
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()
    def result(self) -> int:
        """
        Вычитать текст из поля итоговой суммы
        """
        result = self._driver.find_element(By.CSS_SELECTOR, '[class="screen"]').text
        return result
    