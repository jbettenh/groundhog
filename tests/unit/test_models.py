def test_new_user(new_user):

    assert new_user.username == "jdoe"
    assert new_user.email == "jdoe@groundhog.com"
    assert new_user.name_first == "John"
    assert new_user.name_last == "Doe"


def test_repr(new_user):
    assert repr(new_user) == '<User "jdoe">'


def test_new_sighting(new_sighting):
    assert new_sighting.name == "Sanders Theater"
    assert new_sighting.latitude == 42.375890
    assert new_sighting.longitude == -71.114685
    assert new_sighting.description == "Test sighting"
