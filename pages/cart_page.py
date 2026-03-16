from selenium.webdriver.common.by import By

class CartPage:

    cart_item = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def is_item_present(self):
        items = self.driver.find_elements(*self.cart_item)
        return len(items) > 0