import pytest


@pytest.fixture
def innermost(order, mid):
    order.append("innermost subpackage")


def test_subdir_order(order, top):
    assert order == ["mid subpackage", "innermost subpackage", "top"]


def test_subdir_conf_msf_level(conf_msg_level):
    assert conf_msg_level == 'mid'