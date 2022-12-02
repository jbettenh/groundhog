def test_new_user(new_user):

    assert new_user.username == "jdoe"
    assert new_user.email == "jdoe@groundhog.com"
    assert new_user.name_first == "John"
    assert new_user.name_last == "Doe"


def test_repr(new_user):
    assert repr(new_user) == '<User "jdoe">'
