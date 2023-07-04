import pytest
import util


@pytest.mark.xfail(util.mode() == "mode has bug", reason="mode with bug")
def test_xfail_with_condition():
    assert 0 != 0