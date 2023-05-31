

"""
Creating one log file for each worker
https://pytest-xdist.readthedocs.io/en/stable/how-to.html#creating-one-log-file-for-each-worker
    pytest -n=2 tests/14_plugins/03_parallel/05_log_workers/test_05_parallel_log_workers.py
"""
import logging
import time


def test_parallel_log_workers1():
    logging.info("test_parallel_log_workers1 INFO message")
    time.sleep(1)
    pass


def test_parallel_log_workers2():
    logging.info("test_parallel_log_workers2 INFO message")
    time.sleep(1)
    pass
