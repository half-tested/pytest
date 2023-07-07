import pytest


# Steps to run example:
# 1. initial execution to cache data:
#     pytest tests/08_built_in_fixtures/04_config_cache/test_config_cache.py --cache-clear
# output appears: ...running expensive computation...

# 2. see cache contains cached data
#     pytest --cache-show

# 3. next run fixture reads cached data:
#     pytest tests/08_built_in_fixtures/04_config_cache/test_config_cache.py
# no output due to cached value

# Notes:
# cache data that is JSON serializable
# - works with examples:
#     cache.set("key", "42")
#     cache.set("key", [1, 2, 3])
#     cache.set("key", {"name": "John", "age": 30})
# - TypeError caused on examples:
#     cache.set("key", int)
#     cache.set("my_data", set([1, 2, 3]))
#     cache.set("my_data", file_obj)

def expensive_computation():
    print("\n...running expensive computation...")
    return [1, 2, 3]


@pytest.fixture
def mydata(cache):
    val = cache.get("my_key", None)
    if val is None:
        val = expensive_computation()
        cache.set("my_key", val)
    return val


def test_config_cache(mydata):
    assert mydata == [1, 2, 3]
