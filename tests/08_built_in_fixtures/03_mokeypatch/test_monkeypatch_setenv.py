import os
import pytest


class TestMonkeyUser:

    @pytest.fixture()
    def monkey_user(self, monkeypatch):
        monkeypatch.setenv("USER", "TestingUser")

    def test_monkey_user(self, monkey_user):
        username = os.getenv("USER")
        assert username == "TestingUser"

    def test_regular_user(self):
        username = os.getenv("USER")
        assert username == "TestingUser"

    def test_monkey_(self, monkey_user, monkeypatch):
        assert os.getenv("USER") == "TestingUser"
        monkeypatch.undo()
        assert os.getenv("USER") == "TestingUser"
