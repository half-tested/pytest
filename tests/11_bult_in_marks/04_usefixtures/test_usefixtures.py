import pytest


@pytest.mark.usefixtures("precondition_one", "precondition_two")
def test_usefixtures_mark():
    pass


"""
Other options to use:
1. May specify fixture usage at the test module level using pytestmark:
    pytestmark = pytest.mark.usefixtures("precondition_one", "precondition_two")

2. It is also possible to put fixtures required by all tests in your project into pytest.ini:
    [pytest]
    usefixtures = precondition_one precondition_two
"""
