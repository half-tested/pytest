import pytest

pytestmark = pytest.mark.skip("removed from requirements")


def test_to_skip_by_pytestmark():
    pass


def test_another_skip_by_pytestmark():
    pass
