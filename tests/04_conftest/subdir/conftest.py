import pytest


@pytest.fixture
def mid(order):
    order.append("mid subpackage")
