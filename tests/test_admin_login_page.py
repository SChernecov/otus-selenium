class TestLogin:
    def test_open_admin_login_page(self, browser, admin_login_page):
        admin_login_page.open_admin_login_page(browser)

        admin_login_page.assert_admin_login_page_title(browser)

    def test_login_with_incorrect_credentials(self, browser, admin_login_page):
        admin_login_page.open_admin_login_page(browser)
        admin_login_page.fill_username_and_password(browser)
        admin_login_page.click_login_button(browser)
        admin_login_page.check_alert_wrong_credentials_is_visible(browser)
        admin_login_page.check_alert_wrong_credentials_is_invisible(browser)

        assert browser.current_url.endswith("/admin/"), "Incorrect path in url"
