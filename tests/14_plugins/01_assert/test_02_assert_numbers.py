from assertpy import assert_that


def test_assert_numbers():
    assert_that(123).is_greater_than(100)
    assert_that(123).is_greater_than_or_equal_to(123)
    assert_that(123).is_less_than(200)
    assert_that(123).is_less_than_or_equal_to(200)
    assert_that(123).is_between(100, 200)
    assert_that(123).is_close_to(100, 25)
