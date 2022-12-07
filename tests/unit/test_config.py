def test_development_config(app):
    app.config.from_object("config.DevelopmentConfig")
    assert app.config["FLASK_ENV"] == "development"
    assert app.config["DEBUG"]


def test_production_config(app):
    app.config.from_object("config.ProductionConfig")
    assert app.config["FLASK_ENV"] == "production"
    assert not app.config["DEBUG"]


def test_testing_config(app):
    app.config.from_object("config.TestingConfig")
    assert app.config["FLASK_ENV"] == "testing"
    assert app.config["DEBUG"]
    assert app.config["TESTING"]
