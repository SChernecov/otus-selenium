from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AdminLoginPage:
    UNIQUE_LOCATOR = (By.CSS_SELECTOR, "#header .container-fluid")
    USER_NAME_PLACE_HOLDER = (By.CSS_SELECTOR, "#form-login #input-username")
    PASSWORD_PLACE_HOLDER = (By.CSS_SELECTOR, "#form-login #input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    ALERT_WRONG_CREDENTIAL_LOCATOR = (By.CSS_SELECTOR, ".alert-danger")

    def open_admin_login_page(self, browser, timeout=5):
        try:
            browser.get(browser.url)
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    AdminLoginPage.UNIQUE_LOCATOR))
        except TimeoutException:
            raise AssertionError(
                f"Unique locator:{AdminLoginPage.UNIQUE_LOCATOR[1]} "
                f"not found on the admin login page")

    def assert_admin_login_page_title(self, browser, timeout=5):
        try:
            WebDriverWait(browser, timeout).until(
                EC.title_is("Administration"))
        except TimeoutException:
            raise AssertionError(f"Incorrect browser title:{browser.title}")

    def fill_username_and_password(self, browser, timeout=5):
        try:
            browser.get(browser.url)
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    AdminLoginPage.USER_NAME_PLACE_HOLDER)).send_keys("admin")
        except TimeoutException:
            raise AssertionError(
                f"Currency user name place holder locator:"
                f"{AdminLoginPage.USER_NAME_PLACE_HOLDER[1]} "
                f"not found on the admin login page")
        try:
            browser.get(browser.url)
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    AdminLoginPage.PASSWORD_PLACE_HOLDER)).send_keys("admin")
        except TimeoutException:
            raise AssertionError(
                f"Currency password place holder locator:"
                f"{AdminLoginPage.PASSWORD_PLACE_HOLDER[1]} "
                f"not found on the admin login page")

    def click_login_button(self, browser, timeout=5):
        try:
            browser.get(browser.url)
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    AdminLoginPage.LOGIN_BUTTON)).click()
        except TimeoutException:
            raise AssertionError(
                f"Login button locator:"
                f"{AdminLoginPage.LOGIN_BUTTON[1]} "
                f"not found on the admin login page")

    def check_alert_wrong_credentials_is_visible(self, browser, timeout=5):
        try:
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    AdminLoginPage.ALERT_WRONG_CREDENTIAL_LOCATOR))
        except TimeoutException:
            raise AssertionError(
                f"Wrong credentials alert locator:"
                f"{AdminLoginPage.ALERT_WRONG_CREDENTIAL_LOCATOR[1]} "
                f"not found on the admin login page")

    def check_alert_wrong_credentials_is_invisible(self, browser, timeout=10):
        try:
            WebDriverWait(browser, timeout).until(
                EC.invisibility_of_element_located(
                    AdminLoginPage.ALERT_WRONG_CREDENTIAL_LOCATOR))
        except TimeoutException:
            raise AssertionError(
                f"Wrong credentials alert locator:"
                f"{AdminLoginPage.ALERT_WRONG_CREDENTIAL_LOCATOR[1]} "
                f"not found on the admin login page")
