class TestRegisterPage:

    def test_open_register_page(self, register_page):
        register_page.open()

        assert register_page.title == "Register Account", \
            f"Incorrect browser title:{register_page.browser.title}"

    def test_registration(self, register_page):
        register_page.open()
        register_page.fill_credentials()
        register_page.click_continue_button()

        assert register_page.get_success_registration_text() == \
            "Your Account Has Been Created!\n" \
            "Congratulations! Your new account has been " \
            "successfully created!\n" \
            "You can now take advantage of member privileges to" \
            " enhance your online " \
            "shopping experience with us.\n" \
            "If you have ANY questions about the operation" \
            " of this online shop, please " \
            "e-mail the store owner.\n" \
            "A confirmation has been sent to the provided e-mail" \
            " address. If you have not " \
            "received it within the hour, please contact us.\n" \
            "Continue", \
            "Incorrect success registration text"
