
# Adding a path to python sys.path for importing custom module or library.
# Example creates custom module in temp directory
#   which can be imported later by modifying

import pytest


@pytest.fixture
def mycalculator(tmp_path, monkeypatch):
    module_path = tmp_path / "mycalculator.py"
    module_code = '''
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
                  '''
    module_path.write_text(module_code)

    monkeypatch.syspath_prepend(tmp_path)

    import mycalculator  # IDE warns for no module since it's not installed as usual
    yield mycalculator


def test_mycalculator(mycalculator):
    # Perform assertions or tests on the mycalculator module
    assert mycalculator.add(2, 3) == 5
    assert mycalculator.subtract(5, 2) == 3
    assert mycalculator.multiply(4, 5) == 20
