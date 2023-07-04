import sys

import pytest

if not sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)


def test_skipped_on_module_level_by_pytest_skip():
    pass