import pytest
from pages.main_page import MainPage
from pages.admin_login_page import AdminLoginPage
from pages.register_page import RegisterPage


@pytest.fixture()
def main_page():
    return MainPage()


@pytest.fixture()
def admin_login_page():
    return AdminLoginPage()


@pytest.fixture()
def register_page():
    return RegisterPage()
