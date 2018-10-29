import os
# import psycopg2
from os import urandom

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """ Project environment configurations """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    DATABASE_URL = os.environ['DATABASE_URL']
    # conn = psycopg2.connect(postgresql-adjacent-41807, sslmode='require')

def token_hex(nbytes=None):
    return urandom(nbytes).hex(60)

class DevelopmentConfig(BaseConfig):
    """ enables development environment """
    DEBUG = True
    TESTING = False 
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

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

    