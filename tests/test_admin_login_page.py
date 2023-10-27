class TestLogin:
    def test_open_admin_login_page(self, admin_login_page):
        admin_login_page.open()

        assert admin_login_page.title == "Administration", \
            f"Incorrect browser title:{admin_login_page.browser.title}"

    def test_login_with_incorrect_credentials(self, admin_login_page):
        admin_login_page.open()
        admin_login_page.fill_username_and_password()
        admin_login_page.click_login_button()
        admin_login_page.check_alert_wrong_credentials_is_visible()
        admin_login_page.check_alert_wrong_credentials_is_invisible()

        assert admin_login_page.current_url.endswith(
            "/admin/"), "Incorrect path in url"
