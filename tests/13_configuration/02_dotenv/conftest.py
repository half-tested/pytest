import pytest
import os
from dotenv import load_dotenv


def project_path(request):
    return request.session.fspath.strpath


# load_dotenv()
# bo = load_dotenv("/Users/oleksandrsusla/PycharmProjects/bpy/tests/configuration/02_dotenv/.configuration/.dev.env")

ADMIN_USERNAME = os.environ["admin_username"]
ADMIN_PASSWORD = os.environ["admin_password"]
TEST_USER_USERNAME = os.environ["test_user_username"]
TEST_USER_PASSWORD = os.environ["test_user_password"]
CLIENT_ID = os.environ["client_id"]
CLIENT_SECRET = os.environ["client_secret"]


@pytest.fixture()
def user():
    return TEST_USER_USERNAME, TEST_USER_PASSWORD


@pytest.fixture(autouse=True)
def init():
    print(f"initialize environment using client_id='{CLIENT_ID}', client_secret='{CLIENT_SECRET}'")
    print(f"create configuration using admin_username='{ADMIN_USERNAME}', admin_password='{ADMIN_PASSWORD}'")
