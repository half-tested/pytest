import pytest


@pytest.mark.fast
def test_fast():
    pass


@pytest.mark.fast
@pytest.mark.furious
def test_fast_and_furious():
    pass


@pytest.mark.furious
def test_furious():
    pass


# pytest -m fast
# tests/10_bult_in_marks/06_multiple_markers/test_multiple_markers.py::test_fast PASSED
# tests/10_bult_in_marks/06_multiple_markers/test_multiple_markers.py::test_fast_and_furious PASSED


# pytest -m furious
# tests/10_bult_in_marks/06_multiple_markers/test_multiple_markers.py::test_fast_and_furious PASSED
# tests/10_bult_in_marks/06_multiple_markers/test_multiple_markers.py::test_furious PASSED


# pytest -m "fast and furious"
# tests/10_bult_in_marks/06_multiple_markers/test_multiple_markers.py::test_fast_and_furious PASSED

# pytest -m "fast or furious"
# tests/10_bult_in_marks/06_multiple_markers/test_multiple_markers.py::test_fast PASSED
# tests/10_bult_in_marks/06_multiple_markers/test_multiple_markers.py::test_fast_and_furious PASSED
# tests/10_bult_in_marks/06_multiple_markers/test_multiple_markers.py::test_furious PASSED


# pytest -m "fast and not furious"
# tests/10_bult_in_marks/06_multiple_markers/test_multiple_markers.py::test_fast PASSED
