import pytest
from flask import template_rendered
from groundhog import create_app, db
from groundhog.models import Users, Sightings
from config import TestingConfig


class AuthActions(object):
    def __init__(self, test_client):
        self._client = test_client

    def login(self, username="test", password="password"):
        return self._client.post(
            "/auth/login", data={"username": username, "password": password}
        )

    def logout(self):
        return self._client.get("/auth/logout")


@pytest.fixture(scope="module")
def new_user():
    user = Users("jdoe", "password", "jdoe@groundhog.com", "John", "Doe")
    return user


@pytest.fixture(scope="module")
def new_sighting():
    sighting = Sightings(
        "Sanders Theater", 42.375890, -71.114685, "Test sighting"
    )
    return sighting


@pytest.fixture
def app():
    app = create_app(TestingConfig)

    if app.testing:
        with app.app_context():
            db.drop_all()
            from groundhog.models import Users, Sightings  # noqa: F401

            db.create_all()

            yield app

            db.session.remove()
            if str(db.engine.url) == TestingConfig.SQLALCHEMY_DATABASE_URI:
                db.drop_all()


@pytest.fixture
def test_client(app):
    return app.test_client()


@pytest.fixture
def auth(test_client):
    return AuthActions(test_client)


@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)
