"""Modifying the values of dictionaries e.g. you have a global
configuration that you want to modify for certain test cases"""
DEFAULT_CONFIG = {"user": "user1", "database": "db1"}


def create_connection_string(config=None):

    """Creates a connection string from input or defaults."""
    config = config or DEFAULT_CONFIG
    return f"User Id={config['user']}; Location={config['database']};"


def test_monkey_item(monkeypatch):

    # Patch the values of DEFAULT_CONFIG to specific
    # testing values only for this test.
    monkeypatch.setitem(DEFAULT_CONFIG, "user", "test_user")
    monkeypatch.setitem(DEFAULT_CONFIG, "database", "test_db")

    # expected result based on the mocks
    expected = "User Id=test_user; Location=test_db;"

    # the test uses the monkeypatched dictionary settings
    result = create_connection_string()
    assert result == expected