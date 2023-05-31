import pytest


@pytest.fixture(scope="class")
def setup_class():
    print("\nSetting up class...")


class TestClass:
    def test_class_one(self, setup_class):
        print("Running test_class_one")

    def test_class_two(self, setup_class):
        print("Running test_class_two")
