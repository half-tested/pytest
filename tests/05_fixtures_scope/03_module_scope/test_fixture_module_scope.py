import pytest


@pytest.fixture(scope="module")
def setup_module():
    print("\nSetting up module...")


def test_module_one(setup_module):
    print("Running test_module_one")


def test_module_two(setup_module):
    print("Running test_module_two")
