import pytest


@pytest.mark.xfail(run=False, reason="bug ABC-123")
def test_xfail_math():
    print("won't shown")
    assert 0 != 0