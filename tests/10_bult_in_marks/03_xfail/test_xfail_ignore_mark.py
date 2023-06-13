import pytest


@pytest.mark.xfail(reason="bug ABC-123")
def test_xfail_ignore_mark():
    assert 0 != 0


# pytest --runxfail -k test_xfail_ignore_mark

"""Force the running and reporting of an xfail marked test as if it weren’t marked at all. 
This also causes pytest.xfail() to produce no effect."""
