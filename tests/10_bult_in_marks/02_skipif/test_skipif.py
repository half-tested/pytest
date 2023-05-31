import sys
import pytest


@pytest.mark.skipif(sys.version_info < (3, 20), reason="requires python 3.20 or higher")
def test_simple_skipif():
    pass
