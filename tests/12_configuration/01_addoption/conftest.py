import json
import os

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="test",
        choices=("dev", "test", "stage"),
        dest="env",
        help="environment to work with"
    )
    parser.addoption(
        "--initial-env-setup",
        action="store_true",
        default=False,
        dest="initial-env-setup",
        help="perform initial environment setup"
    )
    parser.addoption(
        "--count",
        action="store",
        default=0,
        type=int,
        help="count of passed items"
    )
    parser.addoption(
        "--item",
        action="append",
        default=[],
        type=float,
        dest="items",
        help="item of single list"
    )


@pytest.fixture()
def env(pytestconfig):
    env = pytestconfig.getoption("env")
    print(f"env={env}")
    return env


@pytest.fixture(autouse=True)
def init_env(pytestconfig, env, admin):
    if not pytestconfig.getoption("initial-env-setup"):
        return
    admin_username, admin_password = admin
    print(f"processing initial setup of '{env}' env with admin creds '{admin_username}' '{admin_password}'")


@pytest.fixture()
def count(request: pytest.FixtureRequest) -> int:
    return request.config.getoption("--count")


@pytest.fixture()
def items(request: pytest.FixtureRequest) -> list:
    return request.config.getoption("items")


@pytest.fixture()
def credentials(env, request: pytest.FixtureRequest):
    return read_config_json(str(request.path.parent), f".configuration/credentials_{env}.json")


@pytest.fixture()
def user(credentials):
    user = credentials["test_user"]
    return user["username"], user["password"]


@pytest.fixture()
def admin(credentials):
    admin = credentials["admin"]
    return admin["username"], admin["password"]


def read_config_json(folder: str, file: str) -> dict:
    print(f"processing file '{file}'")
    config_file = os.path.join(folder, file)
    with open(config_file) as cfg:
        return json.loads(cfg.read())
