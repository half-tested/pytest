import pytest


@pytest.fixture
def order():
    return []


@pytest.fixture
def top(order, innermost):
    order.append("top")


@pytest.fixture
def conf_msg_level():
    return 'top'