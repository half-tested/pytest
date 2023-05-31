import pytest


@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    pass

# pytest -rxXs  # show extra info on xfailed, xpassed, and skipped tests