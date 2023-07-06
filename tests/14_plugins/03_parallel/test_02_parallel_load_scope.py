

"""
CLI option to set distribution algorithm as grouped by module for test functions and by class for test methods:
--dist loadscope
    pytest -n=2 --dist=loadscope tests/14_plugins/03_parallel/test_02_parallel_load_scope.py

Groups are distributed to available workers as whole units.
This guarantees that all tests in a group run in the same process.
This can be useful if you have expensive module-level or class-level fixtures.
Grouping by class takes priority over grouping by module.
"""
import time


def test_parallel_loadscope_test1():
    time.sleep(2)
    pass


def test_parallel_loadscope_test2():
    time.sleep(2)
    pass


class TestClass:
    def test_parallel_loadscope_class_test1(self):
        time.sleep(2)
        pass

    def test_parallel_loadscope_class_test2(self):
        time.sleep(2)
        pass