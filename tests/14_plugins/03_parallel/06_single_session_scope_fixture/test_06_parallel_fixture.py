

"""
Making session-scoped fixtures execute only once.
https://pytest-xdist.readthedocs.io/en/stable/how-to.html#making-session-scoped-fixtures-execute-only-once
    pytest -n=2 tests/14_plugins/03_parallel/06_single_session_scope_fixture/test_06_parallel_fixture.py
"""
import time


def test_parallel_fixture1(session_data):
    assert session_data == 'produced data'
    time.sleep(1)
    pass


def test_parallel_fixture2(session_data):
    assert session_data == 'produced data'
    time.sleep(1)
    pass
