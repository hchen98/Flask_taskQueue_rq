# Flask configure

class Config(object):
    DEBUG = False
    TESTING = False

    DB_NAME = "production-db"
    DB_USERNAME = "admin"
    DB_PASSWORD =  "example"

    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    # inherits the Config class
    # production env
    pass


class DevelopmentConfig(Config):
    # inherits the Config class
    # development env
    DEBUG = True

    DB_NAME = "development-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    # inherits the Config class
    # testing env
    TESTING = True

    DB_NAME = "development-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

    SESSION_COOKIE_SECURE = False