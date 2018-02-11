import itsdangerous
import pytest
import time

from ru_alumni import application
from ru_alumni import token_utils


application.config.from_object('ru_alumni.config.TestingConfig')

TEST_OBJ = {
    'email_address': 'test@python.com',
}
TEST_SHORTENED_EXPIRATION_TIME = 0.100  # 100 ms


@pytest.fixture
def shorten_token_expiration():
    """
    Temporarily shortens the token confirmation expiration time.
    """
    original_expiration_time = application.config['TOKEN_EXPIRATION']
    application.config['TOKEN_EXPIRATION'] = TEST_SHORTENED_EXPIRATION_TIME
    yield
    application.config['TOKEN_EXPIRATION'] = original_expiration_time


class TestTokenUtil():

    def test_happy_case(self):
        token = token_utils.generate_token(TEST_OBJ)
        assert TEST_OBJ == token_utils.confirm_token(token)

    def test_signature_expired(self, shorten_token_expiration):
        token = token_utils.generate_token(TEST_OBJ)
        time.sleep(10 * TEST_SHORTENED_EXPIRATION_TIME)

        # expect to raise exception
        with pytest.raises(itsdangerous.SignatureExpired):
            token_utils.confirm_token(token)

    def test_bad_salt(self):
        token = token_utils.generate_token(TEST_OBJ)

        original_salt = application.config['TOKEN_SALT']
        application.config['TOKEN_SALT'] = 'pepper'

        with pytest.raises(itsdangerous.BadSignature):
            token_utils.confirm_token(token)

        application.config['TOKEN_SALT'] = original_salt

    def test_bad_secret_key(self):
        token = token_utils.generate_token(TEST_OBJ)

        original_secret = application.config['TOKEN_SECRET_KEY']
        application.config['TOKEN_SECRET_KEY'] = 'wrong_key'

        with pytest.raises(itsdangerous.BadSignature):
            token_utils.confirm_token(token)

        application.config['TOKEN_SECRET_KEY'] = original_secret
