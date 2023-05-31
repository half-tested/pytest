import pytest


def valid_config():
    return False


def test_skip_with_pytest_skip():
    if not valid_config():
        pytest.skip("unsupported configuration")