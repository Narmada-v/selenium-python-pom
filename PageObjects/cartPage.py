from selenium.webdriver.common.by import By

class CartPage:
    text_product_name_css = "div.inventory_item_name"
    text_product_qty_css = "div.cart_quantity"

    def __init__(self, driver):
        self.driver = driver

    def getProductName(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.text_product_name_css).text

    def getProductQuantity(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.text_product_qty_css).text