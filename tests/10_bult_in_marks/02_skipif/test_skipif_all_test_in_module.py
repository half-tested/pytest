import sys

import pytest

pytestmark = pytest.mark.skipif(sys.platform != "win32", reason="tests for windows only")


def test_skipped_by_module_scope_mark():
    pass


def test_two_skipped_by_module_scope_mark():
    pass
