import pytest
# markers can be listed in one place
# and be imported in test files

req_change_skip = pytest.mark.skip("requirements changed")
in_development = pytest.mark.skip("still in dev")
never_fix_minors = pytest.mark.skip("minors which never be fixed")