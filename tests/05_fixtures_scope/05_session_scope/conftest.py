import pytest


@pytest.fixture(scope="session")
def setup_session():
    print("\nSetting up session fixture...")