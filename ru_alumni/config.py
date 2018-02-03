import os


class BaseConfig():
    """Base configuration."""
    DEBUG = False

    # token config
    TOKEN_SALT = 'salty'
    TOKEN_SECRET_KEY = 'secret'
    TOKEN_EXPIRATION = 5 * 60  # five mins


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
