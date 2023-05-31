import pytest


@pytest.fixture(autouse=False)
def auto_used_from_conftest():
    print("fixture from conftest invoked")