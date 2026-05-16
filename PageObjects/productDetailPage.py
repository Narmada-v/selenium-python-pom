from selenium.webdriver.common.by import By

class ProductDetailPage:
    text_product_name_css = "div.inventory_details_name"
    text_product_desc_css = "div.inventory_details_desc"
    text_product_price_css = "div.inventory_details_price"
    image_product_tag = "img"
    button_add_cart_class = "btn_inventory"
    button_shopping_cart_id = "shopping_cart_container"

    def __init__(self, driver):
        self.driver = driver

    def getProductName(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.text_product_name_css).text

    def getProductDesc(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.text_product_desc_css).text

    def getProductPrice(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.text_product_price_css).text

    def getProductImage(self):
        return self.driver.find_element(By.TAG_NAME, self.image_product_tag).get_attribute("src")

    def clickAddCartButton(self):
        self.driver.find_element(By.CLASS_NAME, self.button_add_cart_class).click()

    def clickCartButton(self):
        self.driver.find_element(By.ID, self.button_shopping_cart_id).click()