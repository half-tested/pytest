from assertpy import assert_that


def test_assert_lists():
    assert_that([]).is_empty()
    assert_that(['a', 'b']).is_not_empty()

    assert_that(['a', 'b']).is_equal_to(['a', 'b'])
    assert_that(['a', 'b']).is_not_equal_to(['b', 'a'])

    assert_that(['a', 'b']).contains('b', 'a')
    assert_that(['a', 'b']).contains_only('a', 'b')

    assert_that(['a', 'b', 'c']).is_sorted()
    assert_that(['c', 'b', 'a']).is_sorted(reverse=True)

    assert_that(['a', 'x', 'x']).contains_duplicates()
    assert_that(['a', 'b', 'c']).does_not_contain_duplicates()