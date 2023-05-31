import pytest


@pytest.fixture
def message():
    return 'fixture content'


@pytest.fixture(name='lue')
def ultimate_answer_to_life_the_universe_and_everything():
    return 42


def test_has_fixture(message, lue):
    assert message == 'fixture content'
    assert lue == 42