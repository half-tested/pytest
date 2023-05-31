import pytest


@pytest.fixture(scope="package")
def setup_package():
    print("\nSetting up package fixture...")