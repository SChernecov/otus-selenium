from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class MainPage:
    UNIQUE_LOCATOR = (By.CSS_SELECTOR, "main #common-home")

    CURRENCY_DROP_DAWN_LOCATOR = (By.CSS_SELECTOR,
                                  "form .dropdown")
    CURRENCY_EUR_LOCATOR = (
        By.CSS_SELECTOR, "#form-currency li:nth-of-type(1) .dropdown-item")

    CURRENCY_VALUE_LOCATOR = (By.CSS_SELECTOR, "form .dropdown strong")
    DESKTOPS_TAB_LOCATOR = (
        By.CSS_SELECTOR, ".container .nav-item.dropdown:nth-of-type(1)")
    SHOW_ALL_DESKTOPS_LOCATOR = (
        By.CSS_SELECTOR,
        ".container .nav-item.dropdown:nth-of-type(1) .see-all")
    PRODUCT_CATEGORY_LINK = (
        By.CSS_SELECTOR, "#product-category .breadcrumb-item:nth-of-type(2) a")
    MACBOOK_LINK = (
        By.CSS_SELECTOR,
        ".col.mb-3:nth-of-type(1) .product-thumb .description h4 a")

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#form-product div button")

    ALERT_ADD_TO_CARD = (By.CSS_SELECTOR, ".alert.alert-success")
    ALERT_ADD_TO_CARD_TEXT = (By.CSS_SELECTOR, "div#alert")
    CART_TEXT = (
        By.CSS_SELECTOR, "#header-cart .btn-inverse")

    def open_main_page(self, browser, timeout=5):
        try:
            browser.get(browser.url)
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(MainPage.UNIQUE_LOCATOR))
        except TimeoutException:
            raise AssertionError(
                f"Unique locator:{MainPage.UNIQUE_LOCATOR[1]} "
                f"not found on the main page")

    def assert_main_page_title(self, browser, timeout=5):
        try:
            WebDriverWait(browser, timeout).until(
                EC.title_is("Your Store"))
        except TimeoutException:
            raise AssertionError(f"Incorrect browser title:{browser.title}")

    def click_on_currency_drop_down(self, browser, timeout=5):
        try:
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    MainPage.CURRENCY_DROP_DAWN_LOCATOR)).click()
        except TimeoutException:
            raise AssertionError(
                f"Currency drop dawn locator:"
                f"{MainPage.CURRENCY_DROP_DAWN_LOCATOR[1]} "
                f"not found on the main page")

    def click_on_currency_eur(self, browser, timeout=5):
        try:
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    MainPage.CURRENCY_EUR_LOCATOR)).click()
        except TimeoutException:
            raise AssertionError(
                f"Currency eur locator:"
                f"{MainPage.CURRENCY_EUR_LOCATOR[1]} "
                f"not found on the main page")

    def get_currency_value(self, browser, timeout=5):
        try:
            currency_value = WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    MainPage.CURRENCY_VALUE_LOCATOR)).text
            return currency_value
        except TimeoutException:
            raise AssertionError(
                f"Currency value locator:"
                f"{MainPage.CURRENCY_VALUE_LOCATOR[1]} "
                f"not found on the main page")

    def click_on_desktops_tab(self, browser, timeout=5):
        try:
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    MainPage.DESKTOPS_TAB_LOCATOR)).click()
        except TimeoutException:
            raise AssertionError(
                f"Desktops tab locator:"
                f"{MainPage.DESKTOPS_TAB_LOCATOR[1]} "
                f"not found on the main page")

    def click_on_show_all_desktops(self, browser, timeout=5):
        try:
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    MainPage.SHOW_ALL_DESKTOPS_LOCATOR)).click()
        except TimeoutException:
            raise AssertionError(
                f"Show all desktops locator:"
                f"{MainPage.SHOW_ALL_DESKTOPS_LOCATOR[1]} "
                f"not found on the main page")

    def get_product_directory(self, browser, timeout=5):
        try:
            directory = WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    MainPage.PRODUCT_CATEGORY_LINK)).text
            return directory
        except TimeoutException:
            raise AssertionError(
                f"Product directory link locator:"
                f"{MainPage.PRODUCT_CATEGORY_LINK[1]} "
                f"not found on the main page")

    def click_on_macbook(self, browser, timeout=5):
        try:
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    MainPage.MACBOOK_LINK)).click()
        except TimeoutException:
            raise AssertionError(
                f"Macbook link locator:"
                f"{MainPage.MACBOOK_LINK[1]} "
                f"not found on the main page")

    def click_on_add_to_cart_button(self, browser, timeout=5):
        try:
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    MainPage.ADD_TO_CART_BUTTON)).click()
        except TimeoutException:
            raise AssertionError(
                f"Add to cart button locator:"
                f"{MainPage.ADD_TO_CART_BUTTON[1]} "
                f"not found on the main page")

    def check_alert_add_to_card_is_visible(self, browser, timeout=5):
        try:
            WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(MainPage.ALERT_ADD_TO_CARD))
        except TimeoutException:
            raise AssertionError(
                f"Add to cart alert locator:"
                f"{MainPage.ALERT_ADD_TO_CARD[1]} "
                f"not found on the main page")

    def get_alert_add_to_card_text(self, browser, timeout=5):
        try:
            alert_text = WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    MainPage.ALERT_ADD_TO_CARD_TEXT)).text
            return alert_text
        except TimeoutException:
            raise AssertionError(
                f"Add to cart alert text locator:"
                f"{MainPage.ALERT_ADD_TO_CARD_TEXT[1]} "
                f"not found on the main page")

    def check_alert_add_to_card_is_invisible(self, browser, timeout=10):
        try:
            WebDriverWait(browser, timeout).until(
                EC.invisibility_of_element(MainPage.ALERT_ADD_TO_CARD))
        except TimeoutException:
            raise AssertionError(
                f"Add to cart alert locator:"
                f"{MainPage.ALERT_ADD_TO_CARD[1]} "
                f"found on the main page")

    def get_cart_text(self, browser, timeout=5):
        try:
            cart_text = WebDriverWait(browser, timeout).until(
                EC.visibility_of_element_located(
                    MainPage.CART_TEXT)).text
            return cart_text
        except TimeoutException:
            raise AssertionError(
                f"Cart text locator:"
                f"{MainPage.CART_TEXT[1]} "
                f"not found on the main page")
