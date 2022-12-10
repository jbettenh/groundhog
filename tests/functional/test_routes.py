def test_history_page_error(test_client):

    response = test_client.post("/history")
    assert response.status_code == 405


def test_map_page_error(test_client):

    response = test_client.post("/")
    assert response.status_code == 302


def test_tracking_page_error(test_client):

    response = test_client.post("/tracking")
    assert response.status_code == 405


def test_zoo_page_error(test_client):

    response = test_client.post("/zoo")
    assert response.status_code == 405
