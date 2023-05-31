import pytest


@pytest.mark.xfail(strict=False)
def test_xfail_strict():
    assert False


"""
This will make `XPASS` (“unexpectedly passing”) results from this test to fail the test suite.

Parameter strict can be configured in pytest.ini: 
xfail_strict=true
"""
