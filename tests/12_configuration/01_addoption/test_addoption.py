# pytest tests/12_configuration/01_addoption/test_addoption.py --env=stage
# pytest tests/12_configuration/01_addoption/test_addoption.py --env=dev --initial-env-setup
# pytest tests/12_configuration/01_addoption/test_addoption.py --item=2 --item=3.4 --count=2
# pytest tests/12_configuration/01_addoption/test_addoption.py --env=stage --item=2 --item=3.4 --count=2
def test_addoption(user, items, count, env):
    user_username, user_password = user
    print(f"performing test with user '{user_username}' '{user_password}'")
    assert env in user_username
    assert env in user_password

    print(f"items={items}")
    print(f"count={count}")
    assert len(items) == count