import os

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mechanic.db'
    DEBUG = True

class TestingConfig:
    pass

class ProductionConfig:
    pass