from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CalculatorPage import CalculatorPage
def test_calculator_page():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calculator_page = CalculatorPage(driver)
    calculator_page.input_timer(45)
    calculator_page.click7()
    calculator_page.click_add()
    calculator_page.click8()
    calculator_page.click_equals()
    wait = WebDriverWait(driver, 48)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[class="screen"]'), '15'))
    result = calculator_page.result()
    assert result == '15'
    driver.quit()