import pytest


@pytest.fixture(autouse=True)
def config(request: pytest.FixtureRequest):
    print('\nrequest.node.nodeid =', request.node.nodeid)
    print('request.path =', request.path)
    print('request.fixturenames =', request.fixturenames)
    print("request.config.getini('addopts') =", request.config.getini('addopts'))


def test_request_fixture_skip_by_missing_option(request: pytest.FixtureRequest):
    assert request.config.getoption('missing_option', skip=True) == 'will skip'


def test_request_fixture_default_option(request: pytest.FixtureRequest):
    assert request.config.getoption('default_option', default='default_value') == 'default_value'


def test_request_fixture_passed_option(request: pytest.FixtureRequest):
    assert request.config.getoption('-s') == 'no'