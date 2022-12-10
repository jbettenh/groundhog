def test_login_page(test_client):
    response = test_client.get("/auth/login")
    assert response.status_code == 200
    assert b"Log In" in response.data


def test_login_user(test_client):

    response = test_client.post(
        "/auth/login",
        data={
            "username": "test",
            "hash": "passwort",
        },
    )
    assert response.status_code == 302


def test_login_no_username(test_client):

    response = test_client.post(
        "/auth/login",
        data={
            "username": "",
            "hash": "passwort",
        },
    )
    assert response.status_code == 302


def test_login_no_password(test_client):

    response = test_client.post(
        "/auth/login",
        data={
            "username": "Max",
            "hash": "",
        },
    )
    assert response.status_code == 302


def test_logout_page(test_client):

    response = test_client.get("/auth/logout")
    assert response.status_code == 302


def test_logout_page_error(test_client):

    response = test_client.post("/auth/logout")
    assert response.status_code == 405


def test_register_page(test_client):

    response = test_client.get("/auth/register")
    assert response.status_code == 200
    assert b"Sign Up" in response.data


def test_register_user(test_client):

    response = test_client.post(
        "/auth/register",
        data={
            "username": "Max",
            "hash": "passwort",
            "email": "mmuster@groundhog.com",
        },
    )
    assert response.status_code == 302


def test_register_no_username(test_client):

    response = test_client.post(
        "/auth/register",
        data={
            "username": "",
            "password": "passwort",
            "confirmation": "passwort",
            "email": "jdoe@groundhog.com",
        },
    )
    assert response.status_code == 302


def test_register_no_password(test_client):

    response = test_client.post(
        "/auth/register",
        data={
            "username": "Max",
            "password": "",
            "confirmation": "passwort",
            "email": "jdoe@groundhog.com",
        },
    )
    assert response.status_code == 302


def test_register_no_confirmation(test_client):

    response = test_client.post(
        "/auth/register",
        data={
            "username": "Max",
            "password": "passwort",
            "confirmation": "",
            "email": "jdoe@groundhog.com",
        },
    )
    assert response.status_code == 302
