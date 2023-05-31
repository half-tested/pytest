"""
Creating one log file for each worker
"""
import logging
import os

"""
pytest_configure hook:
    Allow plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest file after command line options have been parsed.
    After that, the hook is called for other conftest files as they are imported.
"""


def pytest_configure(config):
    worker_id = os.environ.get("PYTEST_XDIST_WORKER")
    if worker_id is not None:
        logging.basicConfig(
            format=config.getini("log_file_format"),
            filename=f"tests_{worker_id}.log",
            level=config.getini("log_file_level"),
        )
