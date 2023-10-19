from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class RegisterPage:
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


    def open_register_page(self, browser, timeout=5):
        try:
            browser.get(browser.url)
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(RegisterPage.UNIQUE_LOCATOR))
        except TimeoutException:
            raise AssertionError(
                f"Unique locator:{RegisterPage.UNIQUE_LOCATOR[1]} "
                f"not found on the register page")

    def assert_register_page_title(self, browser, timeout=5):
        try:
            WebDriverWait(browser, timeout).until(
                EC.title_is("Register Account"))
        except TimeoutException:
            raise AssertionError(f"Incorrect browser title:{browser.title}")

    def fill_credentials(self, browser, timeout=5):
        import random
        random_int_value = str(random.randint(1000, 9999))
        random_email = random_int_value + "@gmail.com"

        try:
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    RegisterPage.FIRST_NAME_PLACE_HOLDER)).send_keys(
                random_int_value)
        except TimeoutException:
            raise AssertionError(
                f"First name locator:"
                f"{RegisterPage.FIRST_NAME_PLACE_HOLDER[1]} "
                f"not found on the register page")
        try:
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    RegisterPage.LAST_NAME_PLACE_HOLDER)).send_keys(
                random_int_value)
        except TimeoutException:
            raise AssertionError(
                f"Last name locator:"
                f"{RegisterPage.LAST_NAME_PLACE_HOLDER[1]} "
                f"not found on the register page")

        try:
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    RegisterPage.EMAIL_PLACE_HOLDER)).send_keys(
                random_email)
        except TimeoutException:
            raise AssertionError(
                f"Email locator:"
                f"{RegisterPage.EMAIL_PLACE_HOLDER[1]} "
                f"not found on the register page")

        try:
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    RegisterPage.PASSWORD_PLACE_HOLDER)).send_keys(
                random_int_value)
        except TimeoutException:
            raise AssertionError(
                f"Password locator:"
                f"{RegisterPage.PASSWORD_PLACE_HOLDER[1]} "
                f"not found on the register page")

        try:
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    RegisterPage.PRIVATE_POLICY_CHECKBOX)).click()
        except TimeoutException:
            raise AssertionError(
                f"Private policy checkbox locator:"
                f"{RegisterPage.PRIVATE_POLICY_CHECKBOX[1]} "
                f"not found on the register page")

    def click_continue_button(self, browser, timeout=5):
        try:
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    RegisterPage.CONTINUE_BUTTON)).click()
        except TimeoutException:
            raise AssertionError(
                f"Private policy checkbox locator:"
                f"{RegisterPage.CONTINUE_BUTTON[1]} "
                f"not found on the register page")

    def get_success_registration_text(self, browser, timeout=5):
        try:
            success_registration_text = WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    RegisterPage.SUCCESS_REGISTRATION_TEXT)).text
            return success_registration_text
        except TimeoutException:
            raise AssertionError(
                f"Private policy checkbox locator:"
                f"{RegisterPage.CONTINUE_BUTTON[1]} "
                f"not found on the register page")