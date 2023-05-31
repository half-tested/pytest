import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [("3+5", 8), ("2+4", 6), ("6*9", 42)]
)
def test_param_simple(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize(
    argnames="test_input,expected",
    argvalues=[("3+5", 8), ("2+4", 6)],
    ids=["sum check: 3+5=8", "sum check: 2+4=6"]
)
def test_param_with_ids(test_input, expected):
    assert eval(test_input) == expected


params = {
    "argnames": "test_input,expected",
    "argvalues": [("3+5", 8), ("2+4", 6)],
    "ids": ["sum check: 3+5=8", "sum check: 2+4=6"]
}


@pytest.mark.parametrize(**params)
def test_param_by_dict(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
class TestClass:
    def test_class_case(self, n, expected):
        assert n + 1 == expected

    def test_two_class_case(self, n, expected):
        assert (n * 1) + 1 == expected
