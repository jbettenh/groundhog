import pytest
from groundhog import create_app
from groundhog.models import Users


@pytest.fixture(scope="module")
def new_user():
    user = Users("jdoe", "password", "jdoe@groundhog.com", "John", "Doe")
    return user


@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    app.config.from_object("config.TestingConfig")

    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client
