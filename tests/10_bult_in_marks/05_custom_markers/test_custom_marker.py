import pytest

"""
example which adds a command line option and a parametrized 
test function marker to run tests specified via named environments
"""


@pytest.mark.env("stage1")
def test_custom_marker():
    pass

# pytest tests/10_bult_in_marks/05_custom_markers -E stage2
# performs skip

# pytest tests/10_bult_in_marks/05_custom_markers -E stage1
# executes test
