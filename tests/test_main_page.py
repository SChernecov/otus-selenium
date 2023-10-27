from tests.base_test import BaseTest


class TestMainPage(BaseTest):

    def test_main_page_title(self):
        self.main_page.open()

        assert self.main_page.title == "Your Store", \
            f"Incorrect browser title:{self.main_page.title}"

    def test_change_currency_euro(self):
        self.main_page.open()
        self.main_page.click_on_currency_drop_down()
        self.main_page.click_on_currency_eur()

        assert self.main_page.get_currency_value() == "€" \
            , "Incorrect currency value"


class TestCatalog(BaseTest):
    def test_navigate_all_desktops(self):
        self.main_page.open()
        self.main_page.click_on_desktops_tab()
        self.main_page.click_on_show_all_desktops()

        assert self.main_page.get_product_directory() == "Desktops" \
            , "Incorrect product directory"
        assert self.main_page.current_url.endswith("/catalog/desktops") \
            , "Incorrect path in url"


class TestItemCard(BaseTest):
    def test_add_macbook_to_cart(self):
        self.main_page.open()
        self.main_page.click_on_macbook()
        self.main_page.click_on_add_to_cart_button()
        self.main_page.check_alert_add_to_card_is_visible()

        assert self.main_page.get_alert_add_to_card_text() == \
               "Success: You have added MacBook to your shopping cart!" \
            , "Incorrect text in alert add to card"

        self.main_page.check_alert_add_to_card_is_invisible()

        assert self.main_page.get_cart_text() == "1 item(s) - $602.00" \
            , "Incorrect text in cart"
