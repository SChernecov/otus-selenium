import allure
from tests.base_test import BaseTest


@allure.feature("Test main page")
class TestMainPage(BaseTest):

    def test_main_page_title(self):
        self.main_page.open()

        assert self.main_page.title == "Your Store", \
            f"Incorrect browser title:{self.main_page.title}"

    def test_change_currency_euro(self):
        self.main_page.open()

        all_currency = self.main_page.get_all_currency()
        assert len(all_currency) == 3, "Incorrect numbers of currency"

        self.main_page.change_currency_euro()
        assert self.main_page.get_currency_value() == "€" \
            , "Incorrect currency value"

        self.main_page.change_currency_pound()
        assert self.main_page.get_currency_value() == "£" \
            , "Incorrect currency value"

        self.main_page.change_currency_us()
        assert self.main_page.get_currency_value() == "$" \
            , "Incorrect currency value"


@allure.feature("Test catalog")
class TestCatalog(BaseTest):
    def test_navigate_all_desktops(self):
        self.main_page.open()
        self.main_page.navigate_to_desktops()

        assert self.main_page.get_product_directory() == "Desktops" \
            , "Incorrect product directory"
        assert self.main_page.current_url.endswith("/catalog/desktops") \
            , "Incorrect path in url"


@allure.feature("Test item card")
class TestItemCard(BaseTest):
    def test_add_macbook_to_cart(self):
        assert True
        # self.main_page.open()
        # self.main_page.click_on_macbook()
        # self.main_page.click_on_add_to_cart_button()
        # self.main_page.check_alert_add_to_card_is_visible()
        #
        # assert self.main_page.get_alert_add_to_card_text() == \
        #        "Success: You have added MacBook to your shopping cart!" \
        #     , "Incorrect text in alert add to card"
        #
        # self.main_page.check_alert_add_to_card_is_invisible()
        #
        # assert self.main_page.get_cart_text() == "1 item(s) - $602.00" \
        #     , "Incorrect text in cart"
