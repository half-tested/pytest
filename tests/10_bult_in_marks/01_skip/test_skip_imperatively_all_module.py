import sys

import pytest

if not sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)


def test_skipped_on_module_level_by_pytest_skip():
    pass

# pytest -k test_skipped_on_module_level_by_pytest_skip
# pytest tests/10_bult_in_marks/01_skip/test_skip_imperatively_all_module.py