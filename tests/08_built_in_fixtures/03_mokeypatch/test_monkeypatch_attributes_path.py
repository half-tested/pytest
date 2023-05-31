# Modify Path.home() example
from pathlib import Path


def test_monkeypatch_getssh(monkeypatch):
    # mocked return function to replace Path.home
    # always return '/abc'
    def mockreturn():
        return Path("/abc")

    # Application of the monkeypatch to replace Path.home
    # with the behavior of mockreturn defined above.
    monkeypatch.setattr(Path, "home", mockreturn)

    # Init ssh_path will use mockreturn in place of Path.home
    ssh_path = Path.home() / ".ssh"
    assert ssh_path == Path("/abc/.ssh")
