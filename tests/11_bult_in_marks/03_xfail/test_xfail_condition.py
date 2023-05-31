import pytest
import util


@pytest.mark.xfail(util.mode() == "mode has bug", reason="mode with bug")
def test_xfail():
    assert 0 != 0