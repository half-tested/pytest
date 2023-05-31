import pytest


def test_division():
    assert 10 / 5 == 2


def test_zero_division():
    with pytest.raises(ZeroDivisionError) as e:
        assert 10 / 0 == 2
    assert str(e.value) == 'division by zero'


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


# non-default markers registered in pytest.ini
#   - to avoid warnings
#   - to have them listed at single place
# markers =
#     slow: slow tests - no way to speed up
#     flaky: too bad tests - to review
@pytest.mark.slow
def test_is_in():
    assert "a" in "abc"


@pytest.mark.slow
def test_is_not_in():
    assert "d" not in "abc"


def test_floating_point():
    assert 0.1 + 0.2 != 0.3
    assert 0.1 + 0.2 == pytest.approx(0.3)  # approx function performs floating-point comparisons
    assert (0.1 + 0.2, 0.2 + 0.4) == pytest.approx((0.3, 0.6))
    assert {'a': 0.1 + 0.2, 'b': 0.2 + 0.4} == pytest.approx({'a': 0.3, 'b': 0.6})
