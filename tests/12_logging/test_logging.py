import logging
import time
import warnings

import pytest


# pytest tests/12_logging
def test_logging_basic():
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")
    time.sleep(3)


def test_logging_level_per_test(caplog):
    caplog.set_level(logging.DEBUG)
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")