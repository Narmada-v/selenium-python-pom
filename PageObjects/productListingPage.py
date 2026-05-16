from selenium.webdriver.common.by import By

class ProductListingPage:
    text_header_xpath = "//div[@id='header_container']//span[@class='title']"
    text_first_product_name_class = "inventory_item_name"
    text_third_product_name_css = ".inventory_list .inventory_item:nth-of-type(3) .inventory_item_name"
    button_burger_menu_id = "react-burger-menu-btn"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def getHeaderTitle(self):
        return self.driver.find_element(By.XPATH,self.text_header_xpath).text

    def getFirstProductName(self):
        return self.driver.find_element(By.CLASS_NAME, self.text_first_product_name_class).text

    def getThirdProduct(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.text_third_product_name_css)

    def clickBurgerMenu(self):
        self.driver.find_element(By.ID, self.button_burger_menu_id).click()
    
    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()
