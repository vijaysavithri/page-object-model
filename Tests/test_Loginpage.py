import pytest
from pages.Loginpage import LoginPage
from Tests.test_basetest import basetest
from config.config import TestData

class Test_login(basetest):
    def test_signup_link_visible(self):
        self.login_page=LoginPage(self.driver)
        flag=self.login_page.is_signup_link_exist()
        assert flag
    def test_login_page_title(self):
        self.login_page=LoginPage(self.driver)
        title=self.login_page.get_title(TestData.login_page_title)
        assert title==TestData.login_page_title
    def test_login(self):
        self.login_page=LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME,TestData.PASSWORD)

