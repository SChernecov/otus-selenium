from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class AdminLoginPage(BasePage):
    """ Locators """
    UNIQUE_LOCATOR = (By.CSS_SELECTOR, "#header .container-fluid")

    ALERT_WRONG_CREDENTIAL_LOCATOR = (By.CSS_SELECTOR, ".alert-danger")
    ADMIN_PAGE_DASHBOARD_LOCATOR = (By.CSS_SELECTOR, ".page-header h1")
    ALERT_SUCCESS_LOCATOR = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_LICT_CHECKBOX_LOCATOR = (
        By.CSS_SELECTOR, ".table-responsive tbody .form-check-input")

    """ Links """
    CATALOG_LINK = (By.CSS_SELECTOR, "#menu-catalog a[href$='collapse-1']")
    PRODUCTS_LINK = (
        By.CSS_SELECTOR, "#menu-catalog a[href*='product']")
    DATA_TAB_LINK = (By.CSS_SELECTOR, ".nav-tabs a[href$='data']")
    SEO_TAB_LINK = (By.CSS_SELECTOR, ".nav-tabs a[href$='seo']")

    """ Buttons """
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    CLOSE_MODAL_SECURITY_BUTTON = (
        By.CSS_SELECTOR, "#modal-security .btn-close")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#nav-logout .d-md-inline")
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, ".page-header .btn.btn-primary")
    SAVE_BUTTON = (By.CSS_SELECTOR, ".page-header .btn.btn-primary")
    BACK_BUTTON = (By.CSS_SELECTOR, ".page-header .btn.btn-light")
    FILTER_BUTTON = (By.CSS_SELECTOR, "#filter-product #button-filter")
    DELETE_BUTTON = (By.CSS_SELECTOR, ".page-header .btn.btn-danger")

    """ Placeholders """
    USER_NAME_PLACEHOLDER = (By.CSS_SELECTOR, "#form-login #input-username")
    PASSWORD_PLACEHOLDER = (By.CSS_SELECTOR, "#form-login #input-password")
    PRODUCT_NAME_PLACEHOLDER = (By.CSS_SELECTOR, ".tab-content #input-name-1")
    META_TAG_PLACEHOLDER = (
        By.CSS_SELECTOR, ".tab-content #input-meta-title-1")
    MODEL_PLACEHOLDER = (By.CSS_SELECTOR, ".tab-content #input-model")
    KEYWORD_PLACEHOLDER = (
        By.CSS_SELECTOR, ".input-group [placeholder='Keyword']")
    FILTER_PRODUCT_NAME_PLACEHOLDER = (
        By.CSS_SELECTOR, "#filter-product #input-name")
    AUTOCOMPLETE_PLACEHOLDER = (
        By.CSS_SELECTOR, "#filter-product #autocomplete-name")

    def open(self):
        self.open_page(AdminLoginPage.UNIQUE_LOCATOR)

    def login(self, user, password):
        self.send_keys(AdminLoginPage.USER_NAME_PLACEHOLDER, user)
        self.send_keys(AdminLoginPage.PASSWORD_PLACEHOLDER, password)
        self.click(AdminLoginPage.LOGIN_BUTTON)

    def check_alert_wrong_credentials_is_visible(self):
        self.is_element_by_locator_is_visible(
            AdminLoginPage.ALERT_WRONG_CREDENTIAL_LOCATOR)

    def check_alert_wrong_credentials_is_invisible(self):
        self.is_element_by_locator_is_not_visible(
            AdminLoginPage.ALERT_WRONG_CREDENTIAL_LOCATOR)

    def click_modal_security_button(self):
        self.click(AdminLoginPage.CLOSE_MODAL_SECURITY_BUTTON)

    def get_dashboard_text(self):
        return self.get_text(AdminLoginPage.ADMIN_PAGE_DASHBOARD_LOCATOR)

    def click_logout_button(self):
        self.click(AdminLoginPage.LOGOUT_BUTTON)

    def add_product(self, letters):
        self.click(AdminLoginPage.CATALOG_LINK)
        self.click(AdminLoginPage.PRODUCTS_LINK)
        self.click(AdminLoginPage.ADD_NEW_BUTTON)
        self.send_keys(AdminLoginPage.PRODUCT_NAME_PLACEHOLDER, letters)
        self.send_keys(AdminLoginPage.META_TAG_PLACEHOLDER, letters)
        self.click(AdminLoginPage.DATA_TAB_LINK)
        self.send_keys(AdminLoginPage.MODEL_PLACEHOLDER, letters)
        self.click(AdminLoginPage.SEO_TAB_LINK)
        self.send_keys(AdminLoginPage.KEYWORD_PLACEHOLDER, letters)
        self.click(AdminLoginPage.SAVE_BUTTON)

    def check_success_alert_is_visible(self):
        self.is_element_by_locator_is_visible(
            AdminLoginPage.ALERT_SUCCESS_LOCATOR)

    def navigate_to_products(self):
        self.click(AdminLoginPage.BACK_BUTTON)

    def delete_product(self, letters):
        self.send_keys(AdminLoginPage.FILTER_PRODUCT_NAME_PLACEHOLDER, letters)
        self.click(AdminLoginPage.AUTOCOMPLETE_PLACEHOLDER)
        self.click(AdminLoginPage.FILTER_BUTTON)
        self.click(AdminLoginPage.PRODUCT_LICT_CHECKBOX_LOCATOR)
        self.click(AdminLoginPage.DELETE_BUTTON)
        self.accept_alert()
