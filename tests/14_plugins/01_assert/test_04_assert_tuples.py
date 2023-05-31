from assertpy import assert_that


def test_assert_tuples():
    assert_that(()).is_empty()
    assert_that((1, 2, 3)).is_not_empty()

    assert_that((1, 2, 3)).is_not_empty()
    assert_that((1, 2, 3)).is_equal_to((1, 2, 3))
    assert_that((1, 2, 3)).is_not_equal_to((1, 2, 4))

    assert_that((1, 2, 3)).contains(1)
    assert_that((1, 1, 1)).contains_only(1)
    assert_that((1, 2, 3)).contains(3, 2, 1)
    assert_that((1, 2, 3)).does_not_contain(4, 5, 6)
    assert_that((1, 2, 3)).contains_only(1, 2, 3)

    assert_that((1, 2, 3)).is_sorted()
    assert_that((3, 2, 1)).is_sorted(reverse=True)

    assert_that((1, 2, 2)).contains_duplicates()
    assert_that((1, 2, 3)).does_not_contain_duplicates()

    assert_that((1, 2, 3)).starts_with(1)
    assert_that((1, 2, 3)).ends_with(3)