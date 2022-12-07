import pytest


@pytest.mark.skip
def test_zoo_uses_template(test_client, captured_templates):
    response = test_client.get("/zoo")
    template, context = captured_templates[0]

    assert len(captured_templates) == 1
    assert template.name == "zoo.html"
