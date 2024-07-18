from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from shop_pages.MainPage import MainPage
from shop_pages.InventoryPage import InventoryPage
from shop_pages.CartPage import CartPage
from shop_pages.CheckoutPage import CheckoutPage
from shop_pages.OverviewPage import OverviewPage
def test_shop_page():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    shop_page = MainPage(driver)
    shop_page.login('standard_user', 'secret_sauce')
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart('#add-to-cart-sauce-labs-backpack')
    inventory_page.add_to_cart('#add-to-cart-sauce-labs-bolt-t-shirt')
    inventory_page.add_to_cart('#add-to-cart-sauce-labs-onesie')
    inventory_page.click_to_cart()
    cart_page = CartPage(driver)
    cart_page.checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.input_firstname('Вероника')
    checkout_page.input_lastname('Кайбарова')
    checkout_page.input_postalcode('655700')
    checkout_page.click_continue()
    overview_page = OverviewPage(driver)
    total = overview_page.total_price()
    assert total == 'Total: $58.29'
    driver.quit()