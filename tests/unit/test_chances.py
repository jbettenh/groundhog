import pytest
from groundhog.chances import chances


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("USA", "Outlook Good"),
        ("usa", "Outlook Good"),
        ("Canada", "Sorry Canada"),
        ("caNaDa", "Sorry Canada"),
        ("", "My Sources Say No"),
        ("Germany", "Ask Again Later"),
    ],
)
def test_chances(test_input, expected):
    response = chances(test_input)
    assert response == expected
