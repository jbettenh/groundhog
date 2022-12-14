def test_development_config(app):
    app.config.from_object("config.DevelopmentConfig")
    assert app.config["FLASK_ENV"] == "development"


def test_production_config(app):
    app.config.from_object("config.ProductionConfig")
    assert app.config["FLASK_ENV"] == "production"


def test_testing_config(app):
    app.config.from_object("config.TestingConfig")
    assert app.config["FLASK_ENV"] == "testing"
    assert app.config["TESTING"]
