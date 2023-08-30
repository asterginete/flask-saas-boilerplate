import os

class Config:
    """Base configuration class. Contains default settings."""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///my_saas_app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_secret_key')
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', 'stripe_secret_key_placeholder')

class DevelopmentConfig(Config):
    """Development configuration. Inherits from Config."""
    DEBUG = True

class TestingConfig(Config):
    """Testing configuration. Inherits from Config."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

class ProductionConfig(Config):
    """Production configuration. Inherits from Config."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://user:password@localhost/my_saas_app')

config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
