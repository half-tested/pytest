import random
import sys

import pytest


@pytest.mark.flaky()  # re-runs 1 time by default
def test_rerun_simple():
    assert random.choice([True, False])


@pytest.mark.flaky(reruns=3)  # re-runs 3 times
def test_rerun_simple():
    assert random.choice([True, False])


@pytest.mark.flaky(reruns=4, reruns_delay=4)  # re-runs 4 times with 4 sec delay between attempts
def test_rerun_with_delay():
    assert random.choice([True, False])


@pytest.mark.flaky(reruns=5, condition=sys.platform.startswith("win32") or sys.platform.startswith("darwin"))
def test_rerun_on_condition():
    assert random.choice([True, False])


@pytest.mark.flaky(rerun_except="ValueError")  # re-runs any except ValueError
def test_rerun_except():
    raise ValueError()


@pytest.mark.flaky(reruns=3, only_rerun=["OSError", "ValueError"])  # re-runs only OSError or ValueError
def test_rerun_only():
    raise OSError()
