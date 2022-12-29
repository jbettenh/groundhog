import os
from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, ".env"))


class Config(object):
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        base_dir, "groundhog", "app.db"
    )
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI_POSTGRESQL")
    SQLALCHEMY_ECHO = True
    TEMPLATES_AUTO_RELOAD = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI_POSTGRESQL")
    SQLALCHEMY_ECHO = True
    TESTING = True
