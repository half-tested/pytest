import pytest


@pytest.fixture(scope="session")
def fixture_session_level():
    print("----> Setting up session level fixture...")


@pytest.fixture(scope="package")
def fixture_package_level():
    print("----> Setting up package level fixture...")


@pytest.fixture(scope="module")
def fixture_module_level():
    print("----> Setting up module level fixture...")


@pytest.fixture(scope="class")
def fixture_class_level():
    print("----> Setting up class level fixture...")


@pytest.fixture(scope="function")
def fixture_function_level():
    print("----> Setting up function level fixture...")