import pytest


@pytest.fixture
def message():
    return 'fixture content'


def test_has_fixture(message):
    assert message == 'fixture content'