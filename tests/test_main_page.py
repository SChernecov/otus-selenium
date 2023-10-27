class TestMainPage:

    def test_main_page_title(self, main_page):
        main_page.open()

        assert main_page.title == "Your Store", \
            f"Incorrect browser title:{main_page.browser.title}"

    def test_change_currency_euro(self, main_page):
        main_page.open()
        main_page.click_on_currency_drop_down()
        main_page.click_on_currency_eur()

        assert main_page.get_currency_value() == "€" \
            , "Incorrect currency value"


class TestCatalog:
    def test_navigate_all_desktops(self, main_page):
        main_page.open()
        main_page.click_on_desktops_tab()
        main_page.click_on_show_all_desktops()

        assert main_page.get_product_directory() == "Desktops" \
            , "Incorrect product directory"
        assert main_page.current_url.endswith("/catalog/desktops") \
            , "Incorrect path in url"


class TestItemCard:
    def test_add_macbook_to_cart(self, main_page):
        main_page.open()
        main_page.click_on_macbook()
        main_page.click_on_add_to_cart_button()
        main_page.check_alert_add_to_card_is_visible()

        assert main_page.get_alert_add_to_card_text() == \
               "Success: You have added MacBook to your shopping cart!" \
            , "Incorrect text in alert add to card"

        main_page.check_alert_add_to_card_is_invisible()

        assert main_page.get_cart_text() == "1 item(s) - $602.00" \
            , "Incorrect text in cart"
