import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--stringinput",
        action="append",
        default=[],
        help="list of stringinputs to pass to test functions",
    )


# hook is called when collecting a test function
# has metafunc object for parametrization
def pytest_generate_tests(metafunc):
    # if test has fixture then parametrize
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize(argnames="stringinput", argvalues=metafunc.config.getoption("stringinput"))
