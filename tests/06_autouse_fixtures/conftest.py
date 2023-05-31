import pytest


@pytest.fixture(autouse=True, scope='module')
def auto_used_from_conftest():
    print("fixture from conftest invoked")