from config.config import TestData
from pages.Basepage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    email=(By.ID,"login1")
    password=(By.ID,"password")
    login_button=(By.NAME,"proceed")
    signup_link=(By.LINK_TEXT,"Create a new account")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    def get_login_page_title(self,title):
        return self.get_title(title)
    def is_signup_link_exist(self):
        return self.is_visible(self.signup_link)
    def do_login(self,username,password):
        self.do_send_key(self.email,username)
        self.do_send_key(self.password,password)
        self.do_click(self.login_button)

