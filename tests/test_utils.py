from rolltables.utils import normalize_name


def test_normalize_name():
    assert normalize_name("This is a test") == "this_is_a_test"
