def test_history_page_error(test_client):

    response = test_client.post("/history")
    assert response.status_code == 405


def test_zoo_page_error(test_client):

    response = test_client.post("/zoo")
    assert response.status_code == 405
