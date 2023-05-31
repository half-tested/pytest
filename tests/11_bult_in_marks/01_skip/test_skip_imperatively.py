import pytest


def valid_config():
    return False


def test_function():
    if not valid_config():
        pytest.skip("unsupported configuration")