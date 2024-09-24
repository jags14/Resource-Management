class Config(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'