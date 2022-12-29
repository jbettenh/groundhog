def test_new_sighting(new_sighting):
    assert new_sighting.name == "Sanders Theater"
    assert new_sighting.latitude == 42.375890
    assert new_sighting.longitude == -71.114685
    assert new_sighting.description == "Test sighting"


def test_new_sighting_repr(new_sighting):
    assert repr(new_sighting) == '<Sighting "Sanders Theater">'


def test_new_user(new_user):

    assert new_user.username == "jdoe"
    assert new_user.email == "jdoe@groundhog.com"
    assert new_user.name_first == "John"
    assert new_user.name_last == "Doe"


def test_new_user_repr(new_user):
    assert repr(new_user) == '<User "jdoe">'


def test_new_zoo(new_zoo):
    assert new_zoo.name == "Lincoln Park Zoo"
    assert new_zoo.website == "https://www.lpzoo.org/"
    assert new_zoo.description == "For Wildlife. For All."
    assert not new_zoo.has_groundhog


def test_new_zoo_repr(new_zoo):
    assert repr(new_zoo) == '<Zoo "Lincoln Park Zoo">'
