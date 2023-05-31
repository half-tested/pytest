import pytest


@pytest.fixture
def innermost(order):
    order.append("innermost top")


def test_order(order, top):
    assert order == ["innermost top", "top"]


def test_conf_msf_level(conf_msg_level):
    assert conf_msg_level == 'top'
