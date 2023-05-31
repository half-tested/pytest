from assertpy import assert_that


def test_assert_sorting():
    users = [
        {'user': 'Fred', 'age': 36, 'active': True},
        {'user': 'Bob', 'age': 40, 'active': False},
        {'user': 'Johnny', 'age': 13, 'active': True}
    ]

    assert_that(users).extracting('user', sort='age').is_equal_to(['Johnny', 'Fred', 'Bob'])
    assert_that(users).extracting('user', sort=['active', 'age']).is_equal_to(['Bob', 'Johnny', 'Fred'])
    assert_that(users).extracting('user', sort=lambda x: -x['age']) \
        .is_equal_to(['Bob', 'Fred', 'Johnny'])