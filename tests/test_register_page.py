class TestRegisterPage:

    def test_open_register_page(self, browser, register_page):
        register_page.open_register_page(browser)

        register_page.assert_register_page_title(browser)

    def test_registration(self, browser, register_page):
        register_page.open_register_page(browser)
        register_page.fill_credentials(browser)
        register_page.click_continue_button(browser)

        assert register_page.get_success_registration_text(
            browser) == "Your Account Has Been Created!\n"\
                        "Congratulations! Your new account has been " \
                        "successfully created!\n"\
                        "You can now take advantage of member privileges to" \
                        " enhance your online "\
                        "shopping experience with us.\n"\
                        "If you have ANY questions about the operation" \
                        " of this online shop, please "\
                        "e-mail the store owner.\n"\
                        "A confirmation has been sent to the provided e-mail" \
                        " address. If you have not "\
                        "received it within the hour, please contact us.\n"\
                        "Continue", \
                        "Incorrect success registration text"
