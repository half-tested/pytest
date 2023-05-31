import pytest
import os


@pytest.fixture()
def user():
    test_user_username = os.environ["test_user_username"]
    test_user_password = os.environ["test_user_password"]
    return test_user_username, test_user_password


@pytest.fixture(autouse=True)
def init():
    admin_username = os.environ["admin_username"]
    admin_password = os.environ["admin_password"]
    client_id = os.environ["client_id"]
    client_secret = os.environ["client_secret"]
    print(f"initialize environment using client_id='{client_id}', client_secret='{client_secret}'")
    print(f"create configuration using admin_username='{admin_username}', admin_password='{admin_password}'")
