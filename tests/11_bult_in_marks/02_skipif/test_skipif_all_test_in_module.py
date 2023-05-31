import sys

import pytest

pytestmark = pytest.mark.skipif(sys.platform != "win32", reason="tests for windows only")


def test_to_skip():
    pass


def test_another_skip():
    pass
