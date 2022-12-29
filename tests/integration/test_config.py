def test_default_config(app):
    app.config.from_object("config.Config")
    assert not app.config["TESTING"]
    assert not app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]
    assert "sqlite" in app.config["SQLALCHEMY_DATABASE_URI"]


def test_development_config(app):
    with app.app_context():
        app.config.from_object("config.DevelopmentConfig")
        assert app.config["TEMPLATES_AUTO_RELOAD"]
        assert app.config["SQLALCHEMY_ECHO"]
        assert "postgresql" in app.config["SQLALCHEMY_DATABASE_URI"]


def test_testing_config(app):
    app.config.from_object("config.TestingConfig")
    assert app.config["TESTING"]
    assert app.config["SQLALCHEMY_ECHO"]
    assert "postgresql" in app.config["SQLALCHEMY_DATABASE_URI"]
