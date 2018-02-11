import pytest

from ru_alumni import application
from ru_alumni import email_utils, token_utils
from ru_alumni.email_utils import InvalidEmailException


application.config.from_object('ru_alumni.config.TestingConfig')
email_utils.mail.init_app(application)

TEST_EMAIL = 'alum@rutgers.edu'


class TestEmailUtil():

    def test_non_edu_email(self):
        with pytest.raises(InvalidEmailException):
            email_utils.validate_email_address('alum@rutgers.com')

    def test_incorrect_domain_email(self):
        with pytest.raises(InvalidEmailException):
            email_utils.validate_email_address('alum@notrutgers.edu')

    def test_email_is_valid_happy_case(self):
        email_utils.validate_email_address(TEST_EMAIL)
        assert True

    # TODO: Move this; it is an integ test
    # def test_email_send(self):
    #     with application.app_context():
    #         email_utils.send_email(TEST_EMAIL, 'Hi!', 'aye')
