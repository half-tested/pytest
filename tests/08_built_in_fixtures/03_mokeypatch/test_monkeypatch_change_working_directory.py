# Change working directory to the specified path
import os

import pytest


@pytest.fixture
def change_working_directory(tmp_path, monkeypatch):
    print(f"\ninitial working directory is {os.getcwd()}")
    # change working directory to needed. For example, temp directory
    monkeypatch.chdir(tmp_path)


def test_chdir(change_working_directory):
    print(f"changed working directory is {os.getcwd()}")
