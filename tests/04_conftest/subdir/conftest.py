import pytest


@pytest.fixture
def mid(order):
    order.append("mid subpackage")


@pytest.fixture
def conf_msg_level():
    return 'mid'