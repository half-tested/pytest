import pytest


def test_division():
    assert 10 / 5 == 2


def test_modulus():
    assert 10 % 3 == 1


def test_addition():
    assert 2 + 2 != 4, "addition should work based on REQ-123"
    print("Never do anything after assert. It will not be executed if assert fails.")


# non-default naming conventions should be added to pytest.ini:
# python_files = test_*.py check_*.py
# python_classes = Test Check
# python_functions = test_* check_*
def check_subtraction():
    assert 5 - 3 == 2


def test_multiplication():
    assert 3 * 4 == 12


def test_greater_than():
    assert 5 > 3


def test_less_than():
    assert 2 < 4


def test_equal_to():
    assert 6 == 6


def test_not_equal_to():
    assert 3 != 4


@pytest.mark.slow
def test_is_in():
    assert "a" in "abc"


@pytest.mark.slow
def test_is_not_in():
    assert "d" not in "abc"
