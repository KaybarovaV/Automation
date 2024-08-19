from selenium.webdriver.common.by import By
class OverviewPage:
    """
    Этот класс описывает финишную страницу, где можно посмотреть товар, выбранный для покупки, стоимость каждого товара и итоговую стоимость
    """
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/checkout-step-two.html')
        self._driver.maximize_window()
    def total_price(self) -> str:
        """
        Вычитать текст поля итоговой суммы (summary_total_label)
        """
        total = self._driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
        return total