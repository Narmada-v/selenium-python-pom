from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_id = "user-name"
    textbox_password_id = "password"
    text_wrong_login_id = "login_button_container"
    button_login_xpath  = "/html//input[@id='login-button']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def getLoginButton(self):
        return self.driver.find_element(By.XPATH, self.button_login_xpath).get_attribute("value")

    def getWrongLoginText(self):
        return self.driver.find_element(By.ID, self.text_wrong_login_id).text