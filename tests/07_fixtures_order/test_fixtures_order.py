import pytest


# pytest tests/07_fixtures_order/test_fixtures_order.py --setup-plan

@pytest.fixture(scope='session')
def session_fixture():
    print("\nsession fixture")


@pytest.fixture()
def dependent_fixture(function_fixture):
    print("dependent fixture")


@pytest.fixture()
def function_fixture():
    print("function fixture")


@pytest.fixture(autouse=True)
def autouse_fixture():
    print("autouse fixture")


def test_fixtures_order(dependent_fixture, session_fixture):
    print('test content')
