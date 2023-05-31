# Manipulate with environment variables.
# Provides ability to update, add or prepend values.
import os
import pytest


@pytest.fixture()
def monkey_user(monkeypatch):
    # overwrite existing USER environment variable:
    monkeypatch.setenv("USER", "testinguser")
    print(f"\nmocked USER env is {os.getenv('USER')}")


def test_monkey_update_env(monkey_user):
    username = os.getenv("USER")
    assert username == "testinguser"


def test_monkey_new_env(monkeypatch):
    assert 'MY_PARAM' not in os.environ
    # create new environment variable:
    monkeypatch.setenv("MY_PARAM", "my variable")
    assert os.getenv("MY_PARAM") == "my variable"


def test_monkey_prepend(monkeypatch, tmp_path):
    initial_paths_count = len(os.getenv('PATH').split(":"))
    # add value to environment variable:
    monkeypatch.setenv("PATH", str(tmp_path), prepend=":")
    paths = os.getenv('PATH').split(":")
    assert len(paths) == initial_paths_count + 1
    assert paths[0] == str(tmp_path)


def test_monkey_delete_env(monkeypatch):
    assert 'HOME' in os.environ
    print(f"\nHOME env is {os.getenv('HOME')}")
    monkeypatch.delenv("HOME")
    assert 'HOME' not in os.environ


def test_monkey_delete_env_raises(monkeypatch):
    assert 'MY_PARAM' not in os.environ
    with pytest.raises(KeyError):
        monkeypatch.delenv("MY_PARAM", raising=True)