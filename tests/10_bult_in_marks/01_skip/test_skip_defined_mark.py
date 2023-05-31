import pytest

integration_needed = pytest.mark.skip("cannot be done without integration")


@integration_needed
def test_skip_by_defined_marker():
    pass
