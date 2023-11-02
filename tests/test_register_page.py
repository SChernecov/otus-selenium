from tests.base_test import BaseTest
from models.randoms.fake import random_letters, random_email
from tests.base_test import BaseTestRegisterPage


class TestRegisterPage(BaseTestRegisterPage):

    def test_open_register_page(self):
        self.register_page.open()

        assert self.register_page.title == "Register Account", \
            f"Incorrect browser title:{self.register_page.title}"

    def test_registration(self, create_new_user):
        assert self.register_page.get_success_registration_text() == \
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
