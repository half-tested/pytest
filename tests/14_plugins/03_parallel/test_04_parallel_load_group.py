

"""
CLI option to set distribution algorithm as by the xdist_group mark:
--dist loadgroup
    pytest -n=2 --dist=loadgroup tests/14_plugins/03_parallel/test_04_parallel_load_group.py

Groups are distributed to available workers as whole units.
This guarantees that all tests with same xdist_group name run in the same worker.
"""
import time

import pytest


@pytest.mark.xdist_group(name="group1")
def test_parallel_group1_test1():
    time.sleep(2)
    pass


@pytest.mark.xdist_group(name="group1")
def test_parallel_group1_test2():
    time.sleep(2)
    pass


@pytest.mark.xdist_group(name="group2")
def test_parallel_group2_test1():
    time.sleep(2)
    pass


@pytest.mark.xdist_group(name="group2")
def test_parallel_group2_test2():
    time.sleep(2)
    pass