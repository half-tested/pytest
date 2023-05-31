import pytest

import util

mode_filter = pytest.mark.skipif(
    util.mode() == "mode to skip", reason="test is not applicable for mode - " + util.mode()
)