from assertpy import assert_that


def test_assert_dicts():
    assert_that({}).is_empty()
    assert_that({'a': 1, 'b': 2}).is_not_empty()
    assert_that({'a': 1, 'b': 2}).is_length(2)

    assert_that({'a': 1, 'b': 2}).is_equal_to({'b': 2, 'a': 1})
    assert_that({'a': 1, 'b': 2}).is_not_equal_to({'a': 1, 'b': 3})

    assert_that({'a': 1, 'b': 2}).contains('b', 'a')
    assert_that({'a': 1, 'b': 2}).does_not_contain('x')
    assert_that({'a': 1, 'b': 2}).contains_only('a', 'b')
    assert_that({'a': 1, 'b': 2}).is_subset_of({'a': 1, 'b': 2, 'c': 3})

    assert_that({'a': 1, 'b': 2}).contains_value(1)
    assert_that({'a': 1, 'b': 2}).does_not_contain_value(3, 4)

    assert_that({'a': 1, 'b': 2}).contains_entry({'a': 1})
    assert_that({'a': 1, 'b': 2}).does_not_contain_entry({'a': 2})
