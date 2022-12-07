import pytest
from flask import template_rendered
from testing.postgresql import Postgresql
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
    """ 
    from groundhog.models import db

    db.init_app(app)
    
    """

    with Postgresql() as postgresql:
        app.config["SQLALCHEMY_DATABASE_URI"] = postgresql.url()

    yield app


@pytest.fixture
def test_client(app):
    # init_database(app)
    return app.test_client()


@pytest.fixture(scope="session")
def db(app):
    db.app = app
    db.create_all()

    yield db

    db.session.close()
    db.drop_all()


@pytest.fixture(scope="function", autouse=True)
def session(db):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session_ = db.create_scoped_session(options=options)

    db.session = session_

    yield session_

    transaction.rollback()
    connection.close()
    session_.remove()


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
