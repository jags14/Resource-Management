class Config(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    SECRET_KEY = 'alwaysdaring_14'
    SECURITY_PASSWORD_SALT = "thisissalt"
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
    WTF_CSRF_ENABLED = False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authentication-Token'