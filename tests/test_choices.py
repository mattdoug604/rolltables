from rolltables.database import Choice


def test_choices():
    choice = Choice("test", 2.0)
    assert choice.value == "test"
    assert choice.weight == 2.0
