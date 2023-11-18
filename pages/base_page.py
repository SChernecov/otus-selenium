import allure
from selenium.common import WebDriverException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_ELEMENT_TIMEOUT = 5
PAGE_LOAD_TIMEOUT = 30


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.browser.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
        self.logger = browser.logger
        self.class_name = type(self).__name__

    @property
    def current_url(self):
        self.logger.debug(
            "%s: Return current browser url" % (self.class_name))
        return self.browser.current_url

    @property
    def title(self):
        self.logger.debug(
            "%s: Return current browser title" % (self.class_name))
        return self.browser.title

    def wait(self, timeout=None):
        self.logger.debug(
            "%s: Wait" % (self.class_name))
        if timeout is None:
            timeout = WAIT_ELEMENT_TIMEOUT
        return WebDriverWait(self.browser, timeout=timeout)

    @allure.step
    def open_page(self, locator):
        self.logger.debug(
            "%s: Open page: %s" % (self.class_name, str(locator)))
        try:
            self.browser.get(self.browser.url)
            try:
                self.find(locator)
            except TimeoutException:
                raise AssertionError(f"Not found locator: {locator}")
        except Exception:
            raise WebDriverException()

        return self

    @allure.step
    def find(self, locator):
        self.logger.debug(
            "%s: Find: %s" % (self.class_name, str(locator)))
        try:
            return self.wait().until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Not found locator: {locator}")

    @allure.step
    def finds(self, locators):
        self.logger.debug(
            "%s: Finds: %s" % (self.class_name, str(locators)))
        try:
            return self.wait().until(
                EC.visibility_of_all_elements_located(locators))
        except TimeoutException:
            raise AssertionError(f"Not found locators: {locators}")

    @allure.step
    def click(self, locator):
        self.logger.debug(
            "%s: Clicking element: %s" % (self.class_name, str(locator)))
        self.find(locator).click()

    @allure.step
    def get_text(self, locator):
        self.logger.debug(
            "%s: Get text: %s" % (self.class_name, str(locator)))
        return self.find(locator).text

    def clear(self, locator):
        self.logger.debug(
            "%s: Clear: %s" % (self.class_name, str(locator)))
        self.find(locator).clear()

    @allure.step
    def send_keys(self, locator, text):
        self.logger.debug(
            "%s: Send keys to: %s" % (self.class_name, str(locator)))
        self.clear(locator)
        self.find(locator).send_keys(text)

    @allure.step
    def is_element_by_locator_is_visible(self, locator):
        self.logger.debug(
            "%s: Check visibility of: %s" % (self.class_name, str(locator)))
        return self.find(locator)

    @allure.step
    def is_element_by_locator_is_not_visible(self, locator):
        self.logger.debug(
            "%s: Check invisibility of: %s" % (self.class_name, str(locator)))
        return self.find(locator)

    @allure.step
    def accept_alert(self):
        self.logger.debug(
            "%s: Accept alert" % (self.class_name))
        self.browser.switch_to.alert.accept()
