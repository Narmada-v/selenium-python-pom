import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from PageObjects.loginPage import LoginPage
from PageObjects.productListingPage import ProductListingPage
from PageObjects.productDetailPage import ProductDetailPage
from PageObjects.cartPage import CartPage

class SaucedemoProduct(unittest.TestCase):
    baseUrl = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.browser.get(self.baseUrl)
        time.sleep(5)

    def test_a_success_product_open_detail(self):
        # step to login
        loginPage = LoginPage(self.browser)
        loginPage.setUsername(self.username)
        loginPage.setPassword(self.password)
        loginPage.clickLogin()
        time.sleep(5)
        # assert product available
        productListingPage = ProductListingPage(self.browser)
        third_product_name = productListingPage.getThirdProduct().text
        self.assertEqual("Sauce Labs Bolt T-Shirt", third_product_name)
        # step to open detail page
        productListingPage.getThirdProduct().click()
        time.sleep(5)
        # assert product detail
        productDetailPage = ProductDetailPage(self.browser)
        product_detail_name = productDetailPage.getProductName()
        product_detail_desc = productDetailPage.getProductDesc()
        product_detail_price = productDetailPage.getProductPrice()
        product_detail_image = productDetailPage.getProductImage()
        self.assertEqual(product_detail_name, "Sauce Labs Bolt T-Shirt")
        self.assertIn("Get your testing superhero on with the Sauce Labs bolt T-shirt", product_detail_desc)
        self.assertEqual(product_detail_price, "$15.99")
        self.assertIn("data:image/png;base64", product_detail_image)

    def test_b_success_product_add_tocart(self):
        # step to login
        loginPage = LoginPage(self.browser)
        loginPage.setUsername(self.username)
        loginPage.setPassword(self.password)
        loginPage.clickLogin()
        time.sleep(5)
        # assert product available
        productListingPage = ProductListingPage(self.browser)
        third_product_name = productListingPage.getThirdProduct().text
        self.assertEqual("Sauce Labs Bolt T-Shirt", third_product_name)
        # step to add to cart
        productListingPage.getThirdProduct().click()
        productDetailPage = ProductDetailPage(self.browser)
        productDetailPage.clickAddCartButton()
        productDetailPage.clickCartButton()
        time.sleep(5)
        # assert product in cart
        cartPage = CartPage(self.browser)
        cart_product_name = cartPage.getProductName()
        cart_product_qty = cartPage.getProductQuantity()
        self.assertEqual(cart_product_name, "Sauce Labs Bolt T-Shirt")
        self.assertEqual(cart_product_qty, "1")

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__": 
    # run all test
    unittest.main()