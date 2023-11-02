from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class RegisterPage(BasePage):
    """ Locators """
    UNIQUE_LOCATOR = (By.CSS_SELECTOR, "#account-register")

    FIRST_NAME_PLACEHOLDER = (
        By.CSS_SELECTOR, "#form-register #input-firstname")
    LAST_NAME_PLACEHOLDER = (
        By.CSS_SELECTOR, "#form-register #input-lastname")
    EMAIL_PLACEHOLDER = (By.CSS_SELECTOR, "#form-register #input-email")
    PASSWORD_PLACEHOLDER = (By.CSS_SELECTOR, "#form-register #input-password")
    PRIVATE_POLICY_CHECKBOX_LOCATOR = (
        By.CSS_SELECTOR,
        "#form-register input:nth-of-type(1)[type='checkbox']")
    SUCCESS_REGISTRATION_TEXT_LOCATOR = (
        By.CSS_SELECTOR, "#common-success #content")

    """ Buttons """
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".btn-primary")

    def open(self):
        self.open_page(RegisterPage.UNIQUE_LOCATOR)

    def create_user(self, letters, email):
        self.send_keys(RegisterPage.FIRST_NAME_PLACEHOLDER, letters)
        self.send_keys(RegisterPage.LAST_NAME_PLACEHOLDER, letters)
        self.send_keys(RegisterPage.EMAIL_PLACEHOLDER, email)
        self.send_keys(RegisterPage.PASSWORD_PLACEHOLDER, email)
        self.click(RegisterPage.PRIVATE_POLICY_CHECKBOX_LOCATOR)
        self.click(RegisterPage.CONTINUE_BUTTON)

    def get_success_registration_text(self):
        return self.get_text(RegisterPage.SUCCESS_REGISTRATION_TEXT_LOCATOR)
