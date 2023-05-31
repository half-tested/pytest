import random
import sys

import pytest


"""
CLI options:
--reruns [number]
    maximum number of times for the failed test to run
    pytest --reruns=5 tests/14_plugins/02_rerun
    
--reruns-delay [number]
    delay between reruns in seconds
    pytest --reruns-delay=1 --reruns=5 tests/14_plugins/02_rerun
    
    
--only-rerun [Error]
    rerun only errors
    pytest --only-rerun=AssertionError --reruns=5 tests/14_plugins/02_rerun
    pytest --only-rerun=AssertionError --only-rerun=ValueError --reruns=5 tests/14_plugins/02_rerun
    
    
--rerun-except [Error]
    rerun other errors
    pytest --rerun-except=AssertionError --reruns=5 tests/14_plugins/02_rerun
    pytest --rerun-except=AssertionError --rerun-except=OSError --reruns=5 tests/14_plugins/02_rerun
"""


@pytest.mark.flaky(reruns=5)
def test_rerun():
    assert random.choice([True, False])


@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_rerun_with_delay():
    assert random.choice([True, False])


@pytest.mark.flaky(reruns=5, condition=sys.platform.startswith("win32") or sys.platform.startswith("darwin"))
def test_rerun_on_condition():
    assert random.choice([True, False])
