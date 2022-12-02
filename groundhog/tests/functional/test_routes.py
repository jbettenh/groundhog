def test_index_page(test_client):

    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Hi from index" in response.data


def test_index_page_error(test_client):

    response = test_client.post("/")
    assert response.status_code == 405
    assert b"Hi from index" not in response.data
