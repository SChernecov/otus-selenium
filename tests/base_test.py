import allure
import pytest
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from pages.admin_login_page import AdminLoginPage
from models.randoms.fake import random_letters, random_email


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup_ui(self, browser):
        self.browser = browser

    """ Fixture for screenshots and last url if tests failed """
    @pytest.fixture(autouse=True)
    def ui_report(self, request):
        yield
        if request.node.rep_call.failed:
            self.browser.set_page_load_timeout(1)
            if self.browser.session_id:
                allure.attach(self.browser.get_screenshot_as_png(),
                              "failure.png",
                              attachment_type=allure.attachment_type.PNG)
                allure.attach(self.browser.current_url, name="URL",
                              attachment_type=allure.attachment_type.URI_LIST)

    @property
    def main_page(self):
        return MainPage(self.browser)

    @property
    def register_page(self):
        return RegisterPage(self.browser)

    @property
    def admin_login_page(self):
        return AdminLoginPage(self.browser)


class BaseTestRegisterPage(BaseTest):
    @pytest.fixture()
    def create_new_user(self):
        self.register_page.open_page(RegisterPage.UNIQUE_LOCATOR)
        self.register_page.create_user(random_letters(),
                                       random_email())


class BaseTestAdminPage(BaseTest):
    @pytest.fixture()
    def login_admin_page(self):
        self.admin_login_page.open()
        self.admin_login_page.login("user",
                                    "bitnami")
        self.admin_login_page.click_modal_security_button()

    @pytest.fixture()
    def logout_admin_page(self, login_admin_page):
        self.admin_login_page.click_logout_button()
