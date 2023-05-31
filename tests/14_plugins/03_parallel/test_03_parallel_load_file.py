

"""
CLI option to set distribution algorithm as grouped by their containing file:
--dist loadfile
    pytest -n=2 --dist=loadfile tests/14_plugins/03_parallel/test_03_parallel_load_file.py

Groups are distributed to available workers as whole units.
This guarantees that all tests in a file run in the same worker.
"""
import time


def test_parallel_loadfile_test1():
    time.sleep(2)
    pass


def test_parallel_loadfile_test2():
    time.sleep(2)
    pass


class TestClass:
    def test_parallel_loadfile_class_test1(self):
        time.sleep(2)
        pass

    def test_parallel_loadfile_class_test2(self):
        time.sleep(2)
        pass