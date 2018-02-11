import logging
import os


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read_environ_vars(environ_var_key):
    try:
        return os.environ[environ_var_key]
    except KeyError:
        logger.info(
            'Failed to read environment variable {}'.format(environ_var_key)
        )


class BaseConfig():
    """Base configuration."""
    DEBUG = False
    TESTING = False

    # token config
    TOKEN_EXPIRATION = 5 * 60  # five mins
    TOKEN_SALT = 'salty'
    TOKEN_SECRET_KEY = 'secret'

    # email config
    APPLICATION_USERBASE_DOMAIN = 'rutgers'
    MAIL_PORT = 465
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = read_environ_vars('APPLICATION_MAIL_USERNAME')
    MAIL_PASSWORD = read_environ_vars('APPLICATION_MAIL_PASSWORD')

    MAIL_SENDER = ('RU Alumni', '{}@gmail.com'.format(MAIL_USERNAME))


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True

    # email config
    MAIL_USERNAME = read_environ_vars('APPLICATION_MAIL_USERNAME')
    if not MAIL_USERNAME:
        MAIL_USERNAME = 'test_username'
    MAIL_PASSWORD = read_environ_vars('APPLICATION_MAIL_PASSWORD')
    if not MAIL_PASSWORD:
        MAIL_PASSWORD = 'test_password'


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False

    # token config
    TOKEN_EXPIRATION = 24 * 60 * 60  # 24 hours
