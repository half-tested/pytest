from assertpy import assert_that


def test_assert_filtering():
    users = [
        {'user': 'Fred', 'age': 36, 'active': True},
        {'user': 'Bob', 'age': 40, 'active': False},
        {'user': 'Johnny', 'age': 13, 'active': True}
    ]

    assert_that(users).extracting('user', filter='active') \
        .is_equal_to(['Fred', 'Johnny'])
    assert_that(users).extracting('user', filter={'active': False}) \
        .is_equal_to(['Bob'])
    
    assert_that(users).extracting('user', filter={'age': 36, 'active': True}) \
        .is_equal_to(['Fred'])

    assert_that(users).extracting('user', filter=lambda x: x['age'] > 20) \
        .is_equal_to(['Fred', 'Bob'])
