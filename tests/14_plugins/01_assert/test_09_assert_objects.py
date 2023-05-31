from assertpy import assert_that


def test_assert_objects():
    fred = Person('Fred', 'Smith')
    bob = Person('Bob', 'Barr')
    people = [fred, bob]

    assert_that(people).extracting('first_name').is_equal_to(['Fred', 'Bob'])
    assert_that(people).extracting('first_name').contains('Fred', 'Bob')
    assert_that(people).extracting('first_name').does_not_contain('Charlie')


class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def say_hello(self):
        return 'Hello, %s!' % self.first_name
