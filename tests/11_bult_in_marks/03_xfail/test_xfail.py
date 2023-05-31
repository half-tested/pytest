import pytest


def test_fail():
    assert 0 != 0
# FAILED


@pytest.mark.xfail
def test_xfail():
    assert 0 != 0
# XFAIL


@pytest.mark.xfail
def test_xpass():
    assert 0 == 0
# XPASS


@pytest.mark.xfail(reason="bug ABC-123")
def test_xfail_math():
    assert 0 != 0