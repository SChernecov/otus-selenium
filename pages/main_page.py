from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class MainPage(BasePage):
    """ Locators """
    UNIQUE_LOCATOR = (By.CSS_SELECTOR, "main #common-home")

    CURRENCY_DROP_DAWN_LOCATOR = (By.CSS_SELECTOR,
                                  "form .dropdown")
    CURRENCY_LOCATOR = (
        By.CSS_SELECTOR, "#form-currency .dropdown-item")
    CURRENCY_EUR_LOCATOR = (
        By.CSS_SELECTOR, "#form-currency li:nth-of-type(1) .dropdown-item")
    CURRENCY_POUND_LOCATOR = (
        By.CSS_SELECTOR, "#form-currency li:nth-of-type(2) .dropdown-item")
    CURRENCY_US_LOCATOR = (
        By.CSS_SELECTOR, "#form-currency li:nth-of-type(3) .dropdown-item")

    CURRENCY_VALUE_LOCATOR = (By.CSS_SELECTOR, "form .dropdown strong")
    DESKTOPS_TAB_LOCATOR = (
        By.CSS_SELECTOR, ".container .nav-item.dropdown:nth-of-type(1)")
    SHOW_ALL_DESKTOPS_LOCATOR = (
        By.CSS_SELECTOR,
        ".container .nav-item.dropdown:nth-of-type(1) .see-all")
    ALERT_ADD_TO_CARD_LOCATOR = (By.CSS_SELECTOR, ".alert.alert-success")
    ALERT_ADD_TO_CARD_TEXT_LOCATOR = (By.CSS_SELECTOR, "div#alert")
    CART_TEXT_LOCATOR = (
        By.CSS_SELECTOR, "#header-cart .btn-inverse")

    """ Links """
    PRODUCT_CATEGORY_LINK = (
        By.CSS_SELECTOR, "#product-category .breadcrumb-item:nth-of-type(2) a")
    MACBOOK_LINK = (
        By.CSS_SELECTOR,
        ".col.mb-3:nth-of-type(1) .product-thumb .description h4 a")

    """ Buttons """
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#form-product div button")

    def open(self):
        self.open_page(MainPage.UNIQUE_LOCATOR)

    def get_all_currency(self):
        self.click(MainPage.CURRENCY_DROP_DAWN_LOCATOR)
        all_currency_value = self.finds(MainPage.CURRENCY_LOCATOR)
        self.click(MainPage.CURRENCY_DROP_DAWN_LOCATOR)
        return all_currency_value

    def change_currency_euro(self):
        self.click(MainPage.CURRENCY_DROP_DAWN_LOCATOR)
        self.click(MainPage.CURRENCY_EUR_LOCATOR)

    def change_currency_pound(self):
        self.click(MainPage.CURRENCY_DROP_DAWN_LOCATOR)
        self.click(MainPage.CURRENCY_POUND_LOCATOR)

    def change_currency_us(self):
        self.click(MainPage.CURRENCY_DROP_DAWN_LOCATOR)
        self.click(MainPage.CURRENCY_US_LOCATOR)

    def get_currency_value(self):
        return self.get_text(MainPage.CURRENCY_VALUE_LOCATOR)

    def navigate_to_desktops(self):
        self.find(MainPage.DESKTOPS_TAB_LOCATOR)
        self.click(MainPage.DESKTOPS_TAB_LOCATOR)
        self.click(MainPage.SHOW_ALL_DESKTOPS_LOCATOR)

    def get_product_directory(self):
        return self.get_text(MainPage.PRODUCT_CATEGORY_LINK)

    def click_on_macbook(self):
        self.click(MainPage.MACBOOK_LINK)

    def click_on_add_to_cart_button(self):
        self.click(MainPage.ADD_TO_CART_BUTTON)

    def check_alert_add_to_card_is_visible(self):
        self.is_element_by_locator_is_visible(
            MainPage.ALERT_ADD_TO_CARD_LOCATOR)

    def get_alert_add_to_card_text(self):
        return self.get_text(MainPage.ALERT_ADD_TO_CARD_TEXT_LOCATOR)

    def check_alert_add_to_card_is_invisible(self):
        self.is_element_by_locator_is_not_visible(
            MainPage.ALERT_ADD_TO_CARD_LOCATOR)

    def get_cart_text(self):
        return self.get_text(MainPage.CART_TEXT_LOCATOR)
