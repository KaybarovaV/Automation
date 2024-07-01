from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(30)
waiter = WebDriverWait(driver, 40)

# открыть страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# дождаться загрузки картинок
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), "Done!")
)

# получить значение атрибута src у 3й картинки
imgs = driver.find_elements(By.CSS_SELECTOR, "img")
img = imgs[3]
src = img.get_attribute("src")

# вывести значение в консоль
print(src)

driver.quit()