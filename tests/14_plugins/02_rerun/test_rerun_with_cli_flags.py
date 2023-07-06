import random

"""
CLI options:
--reruns [number]
    maximum number of times for the failed test to run
    pytest tests/14_plugins/02_rerun/test_rerun_with_cli_flags.py --reruns=5
    
--reruns-delay [number]
    delay between reruns in seconds
    pytest tests/14_plugins/02_rerun/test_rerun_with_cli_flags.py --reruns-delay=5 --reruns=5
"""


def test_rerun_with_cli_flags():
    assert random.choice([True, False])
