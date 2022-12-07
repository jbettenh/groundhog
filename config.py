import os

POSTGRES = {
    "user": "postgres",
    "pw": os.environ.get("POSTGRESQL_PASSWORD"),
    "db": "groundhogdb",
    "host": "localhost",
    "port": "5432",
}


class Config(object):
    FLASK_ENV = "default"
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    SESSION_COOKIE_NAME = "hennrikson"
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    TEMPLATES_AUTO_RELOAD = True


class ProductionConfig(Config):
    FLASK_ENV = "production"


class TestingConfig(Config):
    FLASK_ENV = "testing"
    DEBUG = True
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
    """
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES
    )
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    TEMPLATES_AUTO_RELOAD = True
    TESTING = True
    WTF_CSRF_ENABLED = False
