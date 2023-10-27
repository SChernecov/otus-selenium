from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class AdminLoginPage(BasePage):
    UNIQUE_LOCATOR = (By.CSS_SELECTOR, "#header .container-fluid")
    USER_NAME_PLACE_HOLDER = (By.CSS_SELECTOR, "#form-login #input-username")
    PASSWORD_PLACE_HOLDER = (By.CSS_SELECTOR, "#form-login #input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    ALERT_WRONG_CREDENTIAL_LOCATOR = (By.CSS_SELECTOR, ".alert-danger")

    def open(self):
        self.open_page(AdminLoginPage.UNIQUE_LOCATOR)

    def fill_username_and_password(self):
        self.send_keys(AdminLoginPage.USER_NAME_PLACE_HOLDER, "admin")
        self.send_keys(AdminLoginPage.PASSWORD_PLACE_HOLDER, "admin")

    def click_login_button(self):
        self.click(AdminLoginPage.LOGIN_BUTTON)

    def check_alert_wrong_credentials_is_visible(self):
        self.is_element_by_locator_is_visible(
            AdminLoginPage.ALERT_WRONG_CREDENTIAL_LOCATOR)

    def check_alert_wrong_credentials_is_invisible(self):
        self.is_element_by_locator_is_not_visible(
            AdminLoginPage.ALERT_WRONG_CREDENTIAL_LOCATOR)
