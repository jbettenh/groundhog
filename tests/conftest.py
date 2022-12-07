import pytest
from flask import template_rendered
from groundhog import create_app
from groundhog.models import Users, db


class AuthActions(object):
    def __init__(self, test_client):
        self._client = test_client

    def login(self, username="joe", password="1234"):
        return self._client.post(
            "/auth/login", data={"username": username, "password": password}
        )

    def logout(self):
        return self._client.get("/auth/logout")


@pytest.fixture(scope="module")
def new_user():
    user = Users("jdoe", "password", "jdoe@groundhog.com", "John", "Doe")
    return user


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.config.from_object("config.TestingConfig")

    from groundhog.models import db

    db.init_app(app)

    yield app


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
