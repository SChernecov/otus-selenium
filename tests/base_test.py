import pytest
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from pages.admin_login_page import AdminLoginPage

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup_ui(self, browser):
        self.browser = browser

    @property
    def main_page(self):
        return MainPage(self.browser)

    @property
    def register_page(self):
        return RegisterPage(self.browser)

    @property
    def admin_login_page(self):
        return AdminLoginPage(self.browser)
