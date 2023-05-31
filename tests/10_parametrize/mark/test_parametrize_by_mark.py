import pytest
import number_util


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42), (number_util.ten(), 10)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize(argnames="test_input,expected", argvalues=[("3+5", 8), ("2+4", 6)], ids=["sum check: 3+5=8", "sum check: 2+4=6"])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


params = {
    "argnames": "test_input,expected",
    "argvalues": [("3+5", 8), ("2+4", 6)],
    "ids": ["sum check: 3+5=8", "sum check: 2+4=6"]
}


@pytest.mark.parametrize(**params)
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
class TestClass:
    def test_simple_case(self, n, expected):
        assert n + 1 == expected

    def test_weird_simple_case(self, n, expected):
        assert (n * 1) + 1 == expected
