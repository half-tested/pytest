from assertpy import assert_that


def test_assert_strings():
    assert_that('').is_empty()
    assert_that('foo').is_length(3)
    assert_that('foo').is_alpha()
    assert_that('123').is_digit()
    assert_that('foo').is_equal_to_ignoring_case('FOO')
    assert_that('foo').starts_with('f')
    assert_that('foo').ends_with('oo')
    assert_that('123-456-7890').matches(r'\d{3}-\d{3}-\d{4}')