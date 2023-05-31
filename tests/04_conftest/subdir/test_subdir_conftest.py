import pytest


@pytest.fixture
def innermost(order, mid):
    order.append("innermost subpackage")


def test_order(order, top):
    assert order == ["mid subpackage", "innermost subpackage", "top"]


def test_qwerty(qwerty):
    print(qwerty)