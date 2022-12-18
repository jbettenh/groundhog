import os
from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, ".env"))

postgres = {
    "user": "postgres",
    "pw": os.environ.get("POSTGRESQL_PASSWORD"),
    "db": os.environ.get("POSTGRESQL_DB"),
    "host": "localhost",
    "port": "5432",
}

base_dir = os.path.abspath(os.path.dirname(__file__))
db_uri_sqlite = "sqlite:///" + os.path.join(base_dir, "groundhog.db")
db_uri_postgresql = (
    "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % postgres
)


class Config(object):
    FLASK_ENV = "default"
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
    SQLALCHEMY_DATABASE_URI = db_uri_postgresql
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    TESTING = False


class DevelopmentConfig(Config):
    FLASK_ENV = "development"
    SQLALCHEMY_DATABASE_URI = db_uri_postgresql
    TEMPLATES_AUTO_RELOAD = True


class ProductionConfig(Config):
    FLASK_ENV = "production"


class TestingConfig(Config):
    FLASK_ENV = "testing"
    SQLALCHEMY_DATABASE_URI = db_uri_postgresql
    SQLALCHEMY_ECHO = True
    TESTING = True
