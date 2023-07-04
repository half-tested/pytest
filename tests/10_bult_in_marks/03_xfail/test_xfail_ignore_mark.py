import pytest


@pytest.mark.xfail(reason="bug ABC-123")
def test_xfail_ignore_mark():
    assert 0 != 0


# pytest tests/10_bult_in_marks/03_xfail/test_xfail_ignore_mark.py --runxfail

"""Force the running and reporting of an xfail marked test as if it weren’t marked at all. 
This also causes pytest.xfail() to produce no effect."""
