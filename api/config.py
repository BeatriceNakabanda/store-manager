import datetime
import os
from os import urandom
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """ Project environment configurations """
    DEBUG = False
    TESTING = False
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=7)
    JWT_TOKEN_LOCATION = ['cookies']
    
def token_hex(nbytes=None):
    return urandom(nbytes).hex(60)

class DevelopmentConfig(BaseConfig):
    """ enables development environment """
    DEBUG = True


class TestingConfig(BaseConfig):
    """ enables testing environment """
    TESTING = True

class ProductionConfig(BaseConfig):
    pass


env_config = dict(
    development = DevelopmentConfig,
    tesing = TestingConfig,
    production = ProductionConfig
)

    