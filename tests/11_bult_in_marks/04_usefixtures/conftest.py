import pytest


@pytest.fixture()
def precondition_one():
    print('precondition_one')


@pytest.fixture()
def precondition_two():
    print('precondition_two')
