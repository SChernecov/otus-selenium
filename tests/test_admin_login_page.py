from tests.base_test import BaseTestAdminPage
from models.randoms.fake import random_letters


class TestAdminPage(BaseTestAdminPage):
    def test_open_admin_login_page(self):
        self.admin_login_page.open()

        assert self.admin_login_page.title == "Administration", \
            f"Incorrect browser title:{self.admin_login_page.title}"

    def test_login(self, login_admin_page):
        assert self.admin_login_page.get_dashboard_text() == \
               "Dashboard", "Incorrect dashboard text"

    def test_logout(self, logout_admin_page):
        assert self.admin_login_page.title == "Administration", \
            f"Incorrect browser title:{self.admin_login_page.title}"

    def test_login_with_incorrect_credentials(self):
        self.admin_login_page.open()
        self.admin_login_page.login("admin", "admin")
        self.admin_login_page.check_alert_wrong_credentials_is_visible()
        self.admin_login_page.check_alert_wrong_credentials_is_invisible()

        assert self.admin_login_page.current_url.endswith(
            "/admin/"), "Incorrect path in url"

    def test_add_product(self, login_admin_page):
        self.admin_login_page.add_product(random_letters())
        self.admin_login_page.check_success_alert_is_visible()

        assert self.admin_login_page.title == "Products", \
            f"Incorrect browser title:{self.admin_login_page.title}"

    def test_delete_product(self, login_admin_page):
        product_name = random_letters()

        self.admin_login_page.add_product(product_name)
        self.admin_login_page.check_success_alert_is_visible()
        self.admin_login_page.navigate_to_products()
        self.admin_login_page.delete_product(product_name)
        self.admin_login_page.check_success_alert_is_visible()

        assert self.admin_login_page.title == "Products", \
            f"Incorrect browser title:{self.admin_login_page.title}"
