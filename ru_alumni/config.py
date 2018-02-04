import os


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
    MAIL_USERNAME = os.environ['APPLICATION_MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['APPLICATION_MAIL_PASSWORD']

    MAIL_SENDER = ('RU Alumni', '{}@gmail.com'.format(MAIL_USERNAME))


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False

    # token config
    TOKEN_EXPIRATION = 24 * 60 * 60  # 24 hours
