import pytest


@pytest.mark.xfail(run=False, reason="bug ABC-123")
def test_xfail_no_run():
    print("won't shown")
    assert 0 != 0


"""
Running from IDE may cause long console output due to pytest framework's internal execution details.
Shows the stack trace and the internal execution flow of pytest while handling the expected failure. 
It includes details about the pytest internals and the specific test case being executed (test_xfail_math).
"""