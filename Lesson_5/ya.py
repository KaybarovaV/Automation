from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://ya.ru")
driver.get("https://vk.com")


#for x in range(1,10):
 #   driver.back()      вернуться назад
  #  driver.forward()   вернуться вперед
#  driver.refresh()   Обновление страницы
# driver.set_window_size(640, 480)   изменение размера окна


sleep(15)