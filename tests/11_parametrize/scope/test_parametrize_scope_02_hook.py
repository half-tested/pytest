import pytest


@pytest.fixture(scope="function")
def x(request):
    val = request.param[0] * 2
    print("fixture call", "val:", val)
    return val


def pytest_generate_tests(metafunc):
    metafunc.parametrize(argnames="x", argvalues=["a", "b"], indirect=True, scope="function")


def test_first_param_scope(x):
    assert len(x) == 2


def test_second_param_scope(x):
    assert len(x) == 2
