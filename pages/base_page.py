from selenium.common import WebDriverException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_ELEMENT_TIMEOUT = 5
PAGE_LOAD_TIMEOUT = 30


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.browser.set_page_load_timeout(PAGE_LOAD_TIMEOUT)

    @property
    def current_url(self):
        return self.browser.current_url

    @property
    def title(self):
        return self.browser.title

    def wait(self, timeout=None):
        if timeout is None:
            timeout = WAIT_ELEMENT_TIMEOUT
        return WebDriverWait(self.browser, timeout=timeout)

    def open_page(self, locator):
        try:
            self.browser.get(self.browser.url)
            try:
                self.find(locator)
            except TimeoutException:
                raise AssertionError(f"Not found locator: {locator}")
        except Exception:
            raise WebDriverException()

        return self

    def find(self, locator):
        try:
            return self.wait().until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Not found locator: {locator}")

    def finds(self, locators):
        try:
            return self.wait().until(
                EC.visibility_of_all_elements_located(locators))
        except TimeoutException:
            raise AssertionError(f"Not found locators: {locators}")

    def click(self, locator):
        self.find(locator).click()

    def get_text(self, locator):
        return self.find(locator).text

    def clear(self, locator):
        self.find(locator).clear()

    def send_keys(self, locator, text):
        self.clear(locator)
        self.find(locator).send_keys(text)

    def is_element_by_locator_is_visible(self, locator):
        return self.find(locator)

    def is_element_by_locator_is_not_visible(self, locator):
        return self.find(locator)

    def accept_alert(self):
        self.browser.switch_to.alert.accept()
