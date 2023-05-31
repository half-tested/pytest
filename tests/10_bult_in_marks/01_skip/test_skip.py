import pytest
import markers


@pytest.mark.skip(reason="no way of currently testing this")
def test_skip_by_marker():
    pass


integration_needed = pytest.mark.skip("cannot be done without integration")


@integration_needed
def test_skip_by_defined_marker():
    pass


@markers.req_change_skip
def test_skip_by_imported_marker():
    pass