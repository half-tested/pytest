import pytest


@pytest.fixture(scope="function")
def x(request):
    val = request.param[0] * 2
    print("fixture call", "val:", val)
    return val


@pytest.mark.parametrize(argnames="x", argvalues=["a", "b"], indirect=True, scope="class")
class TestClass:
    def test_first_param_scope(self, x):
        assert len(x) == 2

    def test_second_param_scope(self, x):
        assert len(x) == 2
