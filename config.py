import os

POSTGRES = {
    "user": "postgres",
    "pw": os.environ.get("POSTGRESQL_PASSWORD"),
    "db": "groundhogdb",
    "host": "localhost",
    "port": "5432",
}

DB_PATH = os.path.join(os.path.dirname(__file__), "tests", "test.db")
DB_URI = "sqlite:///{}".format(DB_PATH)


class Config(object):
    FLASK_ENV = "default"
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
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
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
