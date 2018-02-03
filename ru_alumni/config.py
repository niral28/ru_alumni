import os


class BaseConfig():
    """Base configuration."""
    DEBUG = False
    TOKEN_SALT = 'salty'
    TOKEN_SECRET_KEY = 'secret'


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
