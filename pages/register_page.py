from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class RegisterPage(BasePage):
    UNIQUE_LOCATOR = (By.CSS_SELECTOR, "#account-register")
    FIRST_NAME_PLACE_HOLDER = (
        By.CSS_SELECTOR, "#form-register #input-firstname")
    LAST_NAME_PLACE_HOLDER = (
        By.CSS_SELECTOR, "#form-register #input-lastname")
    EMAIL_PLACE_HOLDER = (By.CSS_SELECTOR, "#form-register #input-email")
    PASSWORD_PLACE_HOLDER = (By.CSS_SELECTOR, "#form-register #input-password")
    PRIVATE_POLICY_CHECKBOX = (
        By.CSS_SELECTOR,
        "#form-register input:nth-of-type(1)[type='checkbox']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    SUCCESS_REGISTRATION_TEXT = (By.CSS_SELECTOR, "#common-success #content")

    def open(self):
        self.open_page(RegisterPage.UNIQUE_LOCATOR)

    def fill_credentials(self):
        import random
        random_int_value = str(random.randint(1000, 9999))
        random_email = random_int_value + "@gmail.com"
        self.send_keys(RegisterPage.FIRST_NAME_PLACE_HOLDER, random_int_value)
        self.send_keys(RegisterPage.LAST_NAME_PLACE_HOLDER, random_int_value)
        self.send_keys(RegisterPage.EMAIL_PLACE_HOLDER, random_email)
        self.send_keys(RegisterPage.PASSWORD_PLACE_HOLDER, random_int_value)
        self.click(RegisterPage.PRIVATE_POLICY_CHECKBOX)

    def click_continue_button(self):
        self.click(RegisterPage.CONTINUE_BUTTON)

    def get_success_registration_text(self):
        return self.get_text(RegisterPage.SUCCESS_REGISTRATION_TEXT)
