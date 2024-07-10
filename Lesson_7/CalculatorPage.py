from selenium.webdriver.common.by import By


class CalculatorPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._driver.maximize_window()
    def input_timer(self, timer):
        self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(timer)
    def click7(self):
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
    def click_add(self):
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
    def click8(self):
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
    def click_equals(self):
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()
    def result(self):
        result = self._driver.find_element(By.CSS_SELECTOR, '[class="screen"').text
        return result