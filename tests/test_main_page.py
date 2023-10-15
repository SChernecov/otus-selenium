class TestMainPage:
    def test_open_main_page(self, browser, main_page):
        main_page.open_main_page(browser)

        main_page.assert_main_page_title(browser)

    def test_change_currency_euro(self, browser, main_page):
        main_page.open_main_page(browser)
        main_page.click_on_currency_drop_down(browser)
        main_page.click_on_currency_eur(browser)

        assert main_page.get_currency_value(browser) == "€" \
            , "Incorrect currency value"


class TestCatalog:
    def test_navigate_all_desktops(self, browser, main_page):
        main_page.open_main_page(browser)
        main_page.click_on_desktops_tab(browser)
        main_page.click_on_show_all_desktops(browser)

        assert main_page.get_product_directory(browser) == "Desktops" \
            , "Incorrect product directory"
        assert browser.current_url.endswith("/catalog/desktops") \
            , "Incorrect path in url"


class TestItemCard:
    def test_add_macbook_to_cart(self, browser, main_page):
        main_page.open_main_page(browser)
        main_page.click_on_macbook(browser)
        main_page.click_on_add_to_cart_button(browser)
        main_page.check_alert_add_to_card_is_visible(browser)

        assert main_page.get_alert_add_to_card_text(browser) == \
               "Success: You have added MacBook to your shopping cart!" \
            , "Incorrect text in alert add to card"

        main_page.check_alert_add_to_card_is_invisible(browser)

        assert main_page.get_cart_text(browser) == "1 item(s) - $602.00" \
            , "Incorrect text in cart"
