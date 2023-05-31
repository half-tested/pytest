import pytest
import util


@pytest.mark.skipif(util.mode() == "mode to skip", reason="test is not applicable for mode - " + util.mode())
def test_function():
    pass