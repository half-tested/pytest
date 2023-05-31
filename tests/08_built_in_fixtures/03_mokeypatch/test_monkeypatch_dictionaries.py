# Modifying the values of dictionaries e.g. global
# configuration can be modified for certain test cases
import pytest

DEFAULT_CONFIG = {"user": "user1", "password": "password1", "database": "db1"}


def test_monkey_setitem(monkeypatch):
    # Patch the values of DEFAULT_CONFIG to specific
    # testing values only for this test.
    monkeypatch.setitem(DEFAULT_CONFIG, "database", "db2")
    print("\n", DEFAULT_CONFIG)
    assert DEFAULT_CONFIG["database"] == "db2"


def test_monkey_delitem(monkeypatch):
    # If raising is set to True (default) in below command, it raises an exception if the item does not exist.
    monkeypatch.delitem(DEFAULT_CONFIG, "database")
    print("\n", DEFAULT_CONFIG)
    with pytest.raises(KeyError) as exception_info:
        print(DEFAULT_CONFIG["database"])
    assert exception_info.value.args[0] == "database"
