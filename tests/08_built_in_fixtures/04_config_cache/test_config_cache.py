import pytest


# pytest tests/08_built_in_fixtures/04_config_cache/test_config_cache.py --cache-clear
# output appears: ...running expensive computation...
#
# pytest tests/08_built_in_fixtures/04_config_cache/test_config_cache.py
# no output due to cached value

def expensive_computation():
    print("\n...running expensive computation...")


@pytest.fixture
def mydata(cache):
    val = cache.get("example/value", None)
    if val is None:
        expensive_computation()
        val = 42
        cache.set("example/value", val)
    return val


def test_config_cache(mydata):
    assert mydata == 42
