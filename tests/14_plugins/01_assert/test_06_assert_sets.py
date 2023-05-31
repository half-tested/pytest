from assertpy import assert_that


def test_assert_sets():
    assert_that(set([])).is_empty()
    assert_that(set(['a', 'b'])).is_not_empty()
    assert_that(set(['a', 'b'])).is_length(2)

    assert_that(set(['a', 'b'])).is_equal_to(set(['b', 'a']))
    assert_that(set(['a', 'b'])).is_not_equal_to(set(['a', 'x']))

    assert_that(set(['a', 'b'])).contains('a')
    assert_that(set(['a', 'b'])).does_not_contain('x', 'y')
    assert_that(set(['a', 'b'])).is_subset_of(set(['a', 'b', 'c']))