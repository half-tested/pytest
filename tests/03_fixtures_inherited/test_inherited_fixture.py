import pytest


@pytest.fixture()
def hello():
    return 'hello'


@pytest.fixture()
def world():
    return 'world'


@pytest.fixture()
def hello_world(hello, world):
    return f'{hello} {world}'


def test_inherited_fixture(hello_world):
    assert hello_world == 'hello world'
