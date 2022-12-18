from groundhog.helpers import error, get_coordinates, get_geocode


def test_error_handler():
    test_error = error("This is a test", 418)
    assert test_error.status_code == 302


def test_get_coordinates():
    loc = get_coordinates("45.130.83.145")

    assert loc == (40.7425, -73.9877)


def test_get_coordinates_none():
    geocode = get_coordinates("255.255")

    assert geocode == (40.7943793, -73.9719996)


def test_get_geocode():
    address = "96 St, Manhattan, NY, 10020, USA"
    geocode = get_geocode(address)

    assert geocode == (40.7943793, -73.9719996)
