from tests.base_test import BaseTest


class TestLogin(BaseTest):
    def test_open_admin_login_page(self):
        self.admin_login_page.open()

        assert self.admin_login_page.title == "Administration", \
            f"Incorrect browser title:{self.admin_login_page.title}"

    def test_login_with_incorrect_credentials(self):
        self.admin_login_page.open()
        self.admin_login_page.fill_username_and_password()
        self.admin_login_page.click_login_button()
        self.admin_login_page.check_alert_wrong_credentials_is_visible()
        self.admin_login_page.check_alert_wrong_credentials_is_invisible()

        assert self.admin_login_page.current_url.endswith(
            "/admin/"), "Incorrect path in url"
