from groundhog.helpers import error


def test_error_handler():
    test_error = error("This is a test", 418)
    assert test_error.status_code == 302
