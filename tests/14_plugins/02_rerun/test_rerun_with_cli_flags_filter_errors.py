"""
CLI options:
--rerun-except [error]
    re-runs all errors except specified
    pytest tests/14_plugins/02_rerun/test_rerun_with_cli_flags_filter_errors.py --reruns=2 --rerun-except=ValueError --rerun-except=OSError
    
--only-rerun [error]
    re-runs only errors 
    pytest tests/14_plugins/02_rerun/test_rerun_with_cli_flags_filter_errors.py --reruns=3 --only-rerun=ValueError
"""


def test_rerun_with_cli_filter_errors():
    raise ValueError()
