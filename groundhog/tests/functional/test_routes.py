def test_about_page_error(test_client):

    response = test_client.post("/about")
    assert response.status_code == 405


def test_index_page_error(test_client):

    response = test_client.post("/")
    assert response.status_code == 405
    assert b"Hi from index" not in response.data
