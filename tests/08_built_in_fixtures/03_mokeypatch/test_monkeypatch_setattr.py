import os


def test_monkey_attr(monkeypatch):
    """Context manager that returns a new MonkeyPatch object which
    undoes any patching done inside the with block upon exit."""
    with monkeypatch.context() as m:
        m.setattr(os, "getcwd", lambda: "/")
        assert os.getcwd() == "/"
    assert os.getcwd() != "/"