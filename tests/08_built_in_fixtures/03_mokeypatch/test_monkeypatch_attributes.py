import pytest


class MyClass:
    def my_method(self):
        return "Hello, World!"

    my_field = 42


def test_monkeypatch_setattr(monkeypatch):
    obj = MyClass()

    # Patching a method
    def mock_method(self):
        return "Mocked method"

    monkeypatch.setattr(MyClass, "my_method", mock_method)

    assert obj.my_method() == "Mocked method"

    # Patching a field
    monkeypatch.setattr(MyClass, "my_field", 100)

    assert obj.my_field == 100


def test_monkeypatch_delattr(monkeypatch):
    obj = MyClass()

    # Deleting a method
    monkeypatch.delattr(MyClass, "my_method")

    # Attempting to call the deleted method raises an AttributeError
    with pytest.raises(AttributeError):
        obj.my_method()

    # Deleting a field
    monkeypatch.delattr(MyClass, "my_field")

    # Attempting to access the deleted field raises an AttributeError
    with pytest.raises(AttributeError):
        assert obj.my_field
