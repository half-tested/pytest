"""
CLI options:
-n or --numprocesses
    use as many processes as computer has CPU cores:
    pytest -n=auto tests/14_plugins/03_parallel/test_01_parallel_load_default.py
    pass processes number:
    pytest -n=3 tests/14_plugins/03_parallel/test_01_parallel_load_default.py
--dist
    distribution algorithm any test for any worker (load is default):
    pytest -n=2 --dist=load tests/14_plugins/03_parallel/test_01_parallel_load_default.py
--maxprocesses=maxprocesses
    limit the maximum number of workers to process the tests
--max-worker-restart
    maximum number of workers that can be restarted when crashed (set to zero to disable this feature).
"""
import time


def test_parallel_load_test1():
    time.sleep(2)
    pass


def test_parallel_load_test2():
    time.sleep(2)
    pass
