from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import CalculatorPage
from time import sleep

def test_calculator_page():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calculator_page = CalculatorPage(driver)
    calculator_page.input_timer('45')
    calculator_page.click7()
    calculator_page.click_add()
    calculator_page.click8()
    calculator_page.click_equals()
    sleep(47)
    result = calculator_page.result()
    assert result == '15'
    driver.quit()