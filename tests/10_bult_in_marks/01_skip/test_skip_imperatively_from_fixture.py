import pytest


@pytest.fixture()
def env():
    return "bad_env"


@pytest.fixture()
def setup(env):
    if env == "bad_env":
        pytest.skip("not running on bad env")
    pass


def test_skipped_from_fixture(setup):
    pass