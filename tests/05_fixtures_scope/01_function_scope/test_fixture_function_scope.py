import pytest


@pytest.fixture(scope="function")
def setup_function():
    print("\nSetting up function...")


def test_function_one(setup_function):
    print("Running test_function_one")


def test_function_two(setup_function):
    print("Running test_function_two")
