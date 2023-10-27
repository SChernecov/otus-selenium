import pytest
from pages.main_page import MainPage
from pages.admin_login_page import AdminLoginPage
from pages.register_page import RegisterPage




@pytest.fixture()
def main_page(browser):
    return MainPage(browser)


@pytest.fixture()
def admin_login_page(browser):
    return AdminLoginPage(browser)


@pytest.fixture()
def register_page(browser):
    return RegisterPage(browser)
