import pytest
import util

mode_filter = pytest.mark.skipif(
    util.mode() == "mode to skip", reason="test is not applicable for mode - " + util.mode()
)


@mode_filter
def test_skipped_by_created_marker():
    pass