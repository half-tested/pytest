import os

import pytest


def test_context(monkeypatch, tmp_path):
    initial_wd = os.getcwd()
    with monkeypatch.context() as monkey:  # context mocks works only under its code block
        monkey.setattr(os, "getcwd", lambda: str(tmp_path))
        assert os.getcwd() == str(tmp_path)
    assert os.getcwd() == initial_wd


def test_undo(monkeypatch, tmp_path):
    monkeypatch.delattr("os.getcwd")
    with pytest.raises(AttributeError):
        print(os.getcwd())
    monkeypatch.undo()  # undo previous monkeypatch
    print(os.getcwd())