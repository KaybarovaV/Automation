from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# открыть страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# пять раз нажать кнопку Add Element
for i in range(5):
    click = driver.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]')
    click.click()

# собрать со страницы список кнопок Delete
b_delete = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')
print(len(b_delete))

sleep(2)
driver.quit()