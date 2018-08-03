"""Defines configurations for different environments.

Currently, only three configurations are defined:
    *development
    *production
    *testing
Specify the type of environment in shell script by exporting first
before running.
    e.g. export FLASK_CONFIG=development
"""

class Config(object):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'

class TestingConfig(Config):
    TESTING = True
    ENV = 'testing'

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing':TestingConfig,
}