Pytest
=


Contents
-
**&nbsp;&nbsp;&nbsp;** **1. Basic:** **&nbsp;** **[`Naming convention`](#naming-convention)**__,__ **[`Test discovery`](#test-discovery)**__,__ **[`Run tests`](#run-tests)**__,__ **[`Re-run tests`](#re-run-tests)**__,__ **[`CLI flags`](#cli-flags)**__.__  
**&nbsp;&nbsp;&nbsp;** **2. Fixtures:** **&nbsp;**  **[`What is fixture`](#what-is-fixture)**__,__**[`conftest.py`](#conftestpy)**__,__ **[`Fixtures scope`](#fixtures-scope)**__,__ **[`Autouse fixtures`](#autouse-fixtures)**__,__ **[`Fixtures order`](#fixtures-order)**__,__ **[`Built-in fixtures`](#built-in-fixtures)**__,__ **[`yield fixtures`](#combinatorics)**__.__  
**&nbsp;&nbsp;&nbsp;** **3. Marks:** **&nbsp;**  **[`skip`](#skip-mark)**__,__ **[`skipif`](#skipif-mark)**__,__ **[`xfail mark`](#xfail-mark)**__,__ **[`usefixtures mark`](#usefixtures-mark)**__,__ **[`Registering marks`](#registering-marks)**__.__  
**&nbsp;&nbsp;&nbsp;** **4. Parametrization:** **&nbsp;**  **[`Parametrize mark`](#parametrize-mark)**__,__ **[`Fixture parametrization`](#fixture-parametrization)**__,__ **[`pytest_generate_tests`](#pytestgeneratetests)**__.__  
**&nbsp;&nbsp;&nbsp;** **5. Configuration:** **&nbsp;**  **[`pytest.ini`](#pytestini)**__,__ **[`pytest_addoption`](#pytestaddoption)**__,__ **[`pytest-dotenv`](#pytest-dotenv)**__.__  
**&nbsp;&nbsp;&nbsp;** **6. Logging:** **&nbsp;**  **[`Logging levels`](#logging-levels)**__,__ **[`CLI logs`](#cli-logs)**__,__ **[`File logs`](#file-logs)**__,__ **[`Fixture caplog`](#format)**__.__  
**&nbsp;&nbsp;&nbsp;** **7. Plugins:** **&nbsp;**  **[`assertpy`](#assertpy)**__,__ **[`pytest-rerunfailures`](#pytest-rerunfailures)**__,__ **[`pytest-xdist`](#pytest-xdist)**__.__  




[`Naming convention`](#contents)
-
### [`Default naming convention`](https://docs.pytest.org/en/stable/explanation/goodpractices.html#conventions-for-python-test-discovery)
* File. Starts with `test_*.py` or ends with `*_test.py`. Example: `test_home_page_layout.py`.
* Classes. Includes `*Test*`. Example: `TestHomePage`.
* Functions. Starts with `test_`. Example: `test_about_us_section`.
### [`Custom naming convention`](https://docs.pytest.org/en/stable/example/pythoncollection.html#changing-naming-conventions)
Make pytest also look for tests in files that match the `check_*`, `Check` prefixes in classes, and functions and methods that match `*_check`
```ini
[pytest]
python_files = test_*.py check_*.py
python_classes = Test Check
python_functions = test_* check_*
```
**Code examples**: [`test_class_naming.py`](tests/01_basic/test_class_naming.py) [`test_naming.py`](tests/01_basic/test_naming.py)
___
[`Test discovery`](#contents)
--------------
### [`testpaths`](https://docs.pytest.org/en/stable/reference/reference.html#confval-testpaths)
Sets list of directories that should be searched for tests when no specific directories, files or test ids are given in the command line when executing pytest from the rootdir directory
```ini
[pytest]
testpaths = testing doc
```
### [`norecursedirs`](https://docs.pytest.org/en/stable/reference/reference.html#confval-norecursedirs)
Set the directory basename patterns to avoid when recursing for test discovery. Example of how to avoid certain directories:
```ini
[pytest]
norecursedirs = .svn _build tmp*
```
### [`Deselect tests during test collection`](https://docs.pytest.org/en/stable/example/pythoncollection.html#deselect-tests-during-test-collection)
Tests can individually be deselected during collection by passing the `--deselect=item` option. For example, say `tests/foobar/test_foobar_01.py` contains `test_a` and `test_b`. You can run all of the tests within `tests/` except for `tests/foobar/test_foobar_01.py::test_a` by invoking pytest with `--deselect tests/foobar/test_foobar_01.py::test_a`. pytest allows multiple `--deselect` options.

### Prevent discovering specific Test classes
To prevent pytest from discovering classes that start with `Test` by setting a boolean `__test__` attribute to `False`:
```python
# Will not be discovered as a test
class TestClass:
    __test__ = False
```
___
[`Run tests`](#contents)
---------

#### Run tests in a module 
```bash
pytest tests/01_basic/test_naming.py
```
#### Run tests in a directory 
```bash
pytest tests/01_basic/
```
#### Run tests by keyword expressions
This will run tests which contain names that match the given string expression (case-insensitive), which can include Python operators that use filenames, class names and function names as variables.
```bash
# single test
pytest -k "test_multiplication"
```
```bash
# entire class without specific test (may be few tests)
pytest -k "TestNamingClass and not test_class_multiplication"
```
```bash
# entire module without specific test (may be few tests)
pytest -k "test_naming.py and not test_multiplication"
```
#### Run tests by node ids
Each collected test is assigned a unique nodeid which consist of the module filename followed by specifiers like class names, function names and parameters from parametrization, separated by `::` characters.
```bash
pytest tests/01_basic/test_naming.py::test_multiplication
```
```bash
pytest tests/01_basic/test_class_naming.py::TestNamingClass::test_class_multiplication
```
#### Run tests by marker expressions
Will run all tests which are decorated by a mark. For example, with the `@pytest.mark.slow` decorator.
```bash
# deselect with '-m "not slow"'
pytest -m slow
```
___
[`Re-run tests`](#contents)
-
#### Re-run last failed tests only
```bash
pytest --lf, --last-failed 
```
#### Re-run all tests, starting with last failed
```bash
pytest --ff, --failed-first
```
#### Stepwise (runs until the first failure and then stop; next time continue from first failed)
```bash
pytest --sw, --stepwise
```
#### Stepwise skip (ignores one failing test and stop test execution on the second failing test)
```bash
pytest --sw-skip, --stepwise-skip
```
#### Clearing cache content (removes all cache contents at start of test run)
```bash
pytest --cache-clear
```
**Pytest docs**: [`how to re-run failed tests`](https://docs.pytest.org/en/stable/how-to/cache.html#how-to-re-run-failed-tests-and-maintain-state-between-test-runs)
___
[`CLI flags`](#contents)
-
#### Increase verbosity (more detailed output)
```bash
pytest -v, --verbose
```
#### Decrease verbosity
```bash
pytest -q, --quite
```
#### Disable stdout capturing (prints shown in console)
```bash
pytest -s, --capture=no
```
#### Stop at first failure
```bash
pytest -x, --exitfirst
```
#### Collect tests without execution
```bash
pytest --collect-only
```
#### Show N slowest tests (N=0 for all)
```bash
pytest --durations=N
```
#### JUnitXML format files (can be read by Jenkins or other CI/CD tool):
```bash
pytest --junit-xml=path
```
**Pytest docs**: [`full list of command-line-flags`](https://docs.pytest.org/en/stable/reference/reference.html#command-line-flags)
___
[`What is fixture`](#contents)
-
* Provides a defined, reliable and consistent context for the tests
* Is a function decorated with @pytest.fixture
* Used to design preconditions and postconditions
* Can be reused over tests
* Multiple fixtures may be used for test
* Sharing test data between tests

**Code examples**: [`test_simple_fixture.py`](tests/02_fixtures/test_simple_fixture.py) [`test_inherited_fixture.py`](tests/03_fixtures_inherited/test_inherited_fixture.py)  
**Pytest docs**: [`about fixtures`](https://docs.pytest.org/en/stable/explanation/fixtures.html#about-fixtures)
---
[`conftest.py`](#contents)
-
* Serves as a means of providing fixtures for an entire directory
* No need to do import for any test in same package
* Multiple conftest.py may be used as for root and sub-directories
* Defined fixtures may be overwritten in sub-directories

**Code examples**: [`test_conftest.py`](tests/04_conftest/test_conftest.py) [`test_subdir_conftest.py`](tests/04_conftest/subdir/test_subdir_conftest.py)  
**Pytest docs**: [`about conftest.py`](https://docs.pytest.org/en/stable/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files)
___
[`Fixtures scope`](#contents)
-
* function - the default scope, the fixture is destroyed at the end of the test
* class - the fixture is destroyed during teardown of the last test in the class
* module - the fixture is destroyed during teardown of the last test in the module
* package - the fixture is destroyed during teardown of the last test in the package
* session - the fixture is destroyed at the end of the test session

**Code examples**: [`test_fixture_function_scope.py`](tests/05_fixtures_scope/01_function_scope/test_fixture_function_scope.py) [`test_fixture_class_scope.py`](tests/05_fixtures_scope/02_class_scope/test_fixture_class_scope.py) [`test_fixture_module_scope.py`](tests/05_fixtures_scope/03_module_scope/test_fixture_module_scope.py) [`test_01_fixture_package_scope.py`](tests/05_fixtures_scope/04_package_scope/test_01_fixture_package_scope.py) [`test_01_fixture_session_scope.py`](tests/05_fixtures_scope/05_session_scope/01_package/test_01_fixture_session_scope.py)  
**Pytest docs**: [`about fixtures scope`](https://docs.pytest.org/en/stable/how-to/fixtures.html#fixture-scopes)
___
[`Autouse fixtures`](#contents)
-
* Convenient way to make all tests automatically request fixture
* Cut out a lot of redundant requests
* Provide more advanced fixture usage
* autouse=True makes a fixture configured for autouse

**Code examples**: [`test_autouse_fixtures.py`](tests/06_autouse_fixtures/test_autouse_fixtures.py)  
**Pytest docs**: [`about autouse fixtures`](https://docs.pytest.org/en/stable/how-to/fixtures.html#autouse-fixtures-fixtures-you-don-t-have-to-request)
___
[`Fixtures order`](#contents)
-
* Based on 3 factors:
  * scope
  * dependencies
  * autouse
* Higher-scoped fixtures are executed first. Higher-scopes (such as session) are executed before lower-scoped fixtures (such as function or class)
* Fixtures of the same order execute based on dependencies
* Autouse fixtures are executed first within their scope

**Code examples**: [`test_fixtures_order.py`](tests/07_fixtures_order/test_fixtures_order.py)  
**Pytest docs**: [`about fixtures order`](https://docs.pytest.org/en/stable/reference/fixtures.html#fixture-instantiation-order)
___
[`Built-in fixtures`](#contents)
-
#### [`tmp_path`](https://docs.pytest.org/en/stable/how-to/tmp_path.html#the-tmp-path-fixture) and [`tmp_path_factory`](https://docs.pytest.org/en/stable/how-to/tmp_path.html#the-tmp-path-factory-fixture)
Temporary directory unique to the test invocation and session-scope  
**Code examples**: [`test_01_tmp_path.py`](tests/08_built_in_fixtures/01_temp_directory/test_01_tmp_path.py) [`test_02_tmp_path_factory.py`](tests/08_built_in_fixtures/01_temp_directory/test_02_tmp_path_factory.py)  
#### [`request`](https://docs.pytest.org/en/stable/reference/reference.html#request)
Provide information on the executing test function  
**Code examples**: [`test_request_fixture.py`](tests/08_built_in_fixtures/02_request/test_request_fixture.py)
#### [`monkeypatch`](https://docs.pytest.org/en/stable/how-to/monkeypatch.html)
Has helper methods for safely patching and mocking functionality in tests  
**Code examples**: [`test_monkeypatch_setattr.py`](tests/08_built_in_fixtures/03_mokeypatch/test_monkeypatch_setattr.py) [`test_monkeypatch_setenv.py`](tests/08_built_in_fixtures/03_mokeypatch/test_monkeypatch_setenv.py) [`test_monkeypatch_setitem.py`](tests/08_built_in_fixtures/03_mokeypatch/test_monkeypatch_setitem.py)
#### [`cache`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-cache)
Store and retrieve values across pytest runs  
**Code examples**: [`test_config_cache.py`](tests/08_built_in_fixtures/04_config_cache/test_config_cache.py)  
#### [`and other built-in fixtures...`](https://docs.pytest.org/en/stable/reference/fixtures.html#built-in-fixtures)
Capture output or logs; record extra properties; record warnings etc.
___
[`yield fixtures`](#contents)
-
* `return` is swapped out for `yield`
* Any teardown code for that fixture is placed after the yield
* Once the test is finished, pytest will go back down the list of fixtures, but in the reverse order, taking each one that yielded, and running the code inside it that was after the yield statement.

**Code examples**: [`test_yield_fixture.py`](tests/09_yield_fixtures/test_yield_fixture.py)  
**Pytest docs**: [`about yield fixtures`](https://docs.pytest.org/en/stable/how-to/fixtures.html#yield-fixtures-recommended)
___
[`skip mark`](#contents)
-
The simplest way to skip a test function is to mark it with the skip decorator which may be passed an optional reason.  
```python
@pytest.mark.skip(reason="no way of currently testing this")
```
**Code examples**: [`test_skip.py`](tests/11_bult_in_marks/01_skip/test_skip.py) [`test_skip_all_test_in_module.py`](tests/11_bult_in_marks/01_skip/test_skip_all_test_in_module.py) [`test_skip_imperatively.py`](tests/11_bult_in_marks/01_skip/test_skip_imperatively.py) [`test_skip_imperatively_all_module.py`](tests/11_bult_in_marks/01_skip/test_skip_imperatively_all_module.py)  
**Pytest docs**: [`about skip mark`](https://docs.pytest.org/en/stable/how-to/skipping.html#skipping-test-functions)
___
[`skipif mark`](#contents)
-
Skip test conditionally. If the condition evaluates to True during collection, the test function will be skipped.  
```python
@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10")
```
**Code examples**: [`test_skipif.py`](tests/11_bult_in_marks/02_skipif/test_skipif.py) [`test_skipif_all_test_in_module.py`](tests/11_bult_in_marks/02_skipif/test_skipif_all_test_in_module.py) [`test_skipif_defined_mark.py`](tests/11_bult_in_marks/02_skipif/test_skipif_defined_mark.py) [`test_skipif_defined_mark_outside.py`](tests/11_bult_in_marks/02_skipif/test_skipif_defined_mark_outside.py) [`test_skipif_evaluated_condition.py`](tests/11_bult_in_marks/02_skipif/test_skipif_evaluated_condition.py)  
**Pytest docs**: [`about skipif mark`](https://docs.pytest.org/en/stable/how-to/skipping.html#id1)
___
[`xfail mark`](#contents)
-
The xfail marker indicates a test expect to fail.
```python
@pytest.mark.xfail(reason="known parser issue")
```
**Code examples**: [`test_xfail.py`](tests/11_bult_in_marks/03_xfail/test_xfail.py) [`test_xfail_condition.py`](tests/11_bult_in_marks/03_xfail/test_xfail_condition.py) [`test_xfail_ignore_mark.py`](tests/11_bult_in_marks/03_xfail/test_xfail_ignore_mark.py) [`test_xfail_no_run.py`](tests/11_bult_in_marks/03_xfail/test_xfail_no_run.py)  
**Pytest docs**: [`about xfail mark`](https://docs.pytest.org/en/stable/how-to/skipping.html#xfail-mark-test-functions-as-expected-to-fail)
___
[`usefixtures mark`](#contents)
-
Mark a test function as using the given fixture names.
```python
@pytest.mark.usefixtures("perform_config")
```
**Code examples**: [`test_usefixtures.py`](tests/11_bult_in_marks/04_usefixtures/test_usefixtures.py)  
**Pytest docs**: [`about usefixtures mark`](https://docs.pytest.org/en/stable/how-to/fixtures.html#usefixtures)  
___
[`Registering marks`](#contents)
-
#### Custom marks can be registered in pytest.ini file:
```ini
[pytest]
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    serial
```
#### Custom marks can be registered programmatically in a pytest_configure hook
```python
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "env(name): mark test to run only on named environment"
    )
```
**Code examples**: [`test_marks_with_parametrize.py`](tests/11_bult_in_marks/05_with_parametrize/test_marks_with_parametrize.py)  
**Pytest docs**: [`about registering marks`](https://docs.pytest.org/en/stable/how-to/mark.html#registering-marks)
___
[`Parametrize mark`](#contents)
-
The builtin pytest.mark.parametrize decorator enables parametrization of arguments for a test function.
```python
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```
**Code examples**: [`test_parametrize_by_mark.py`](tests/11_parametrize/01_mark/test_parametrize_by_mark.py) [`test_parametrize_module_by_mark.py`](tests/11_parametrize/01_mark/test_parametrize_module_by_mark.py)  
**Pytest docs**: [`about @pytest.mark.parametrize`](https://docs.pytest.org/en/stable/how-to/parametrize.html#pytest-mark-parametrize-parametrizing-test-functions)
___
[`Fixture parametrization`](#contents)
-
Fixture functions can be parametrized in which case they will be called multiple times, each time executing the set of dependent tests, i.e. the tests that depend on this fixture.
```python
@pytest.fixture(scope="module", params=["smtp.gmail.com", "mail.python.org"])
def smtp_connection(request):
    smtp_connection = smtplib.SMTP(request.param, 587, timeout=5)
    yield smtp_connection
    print(f"finalizing {smtp_connection}")
    smtp_connection.close()
```
**Code examples**: [`test_parametrize_by_fixture.py`](tests/11_parametrize/02_fixture/test_parametrize_by_fixture.py)
**Pytest docs**: [`about fixture parametrization`](https://docs.pytest.org/en/stable/how-to/fixtures.html#fixture-parametrize)
___
[`pytest_generate_tests`](#contents)
-
Pytest hook to dynamically generate tests. For example based on command-line options:
```python
# content of conftest.py
def pytest_addoption(parser):
    parser.addoption(
        "--stringinput",
        action="append",
        default=[],
        help="list of stringinputs to pass to test functions",
    )


def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))

# content of test_parametrize_by_generate.py
def test_parametrize_by_generate(stringinput):
    assert stringinput.isalpha()

# pytest tests/11_parametrize/03_generate/test_parametrize_by_generate.py --stringinput="hello" --stringinput="world" --stringinput="4317" -v
```
**Code examples**: [`test_parametrize_by_generate.py`](tests/11_parametrize/03_generate/test_parametrize_by_generate.py)  
**Pytest docs**: [`about pytest_generate_tests`](https://docs.pytest.org/en/stable/how-to/parametrize.html#pytest-generate-tests)
___
[`pytest.ini`](#contents)
-
Pytest configuration options may be written in a pytest.ini (or .pytest.ini). Usually located at the root.
#### testpaths directories to search for tests
```ini
[pytest]
testpaths =
  tests
  integration
```
#### addopts (args) for extra command line options
```ini
[pytest]
addopts = --maxfail=2  # exit after 2 failures
```
#### Add fixtures that will be applied to all test functions according to defined scope
```ini
[pytest]
usefixtures =
    clean_db
```
#### Config options may be overwritten in CLI with option -o/--override-ini
```
pytest -o console_output_style=classic -o cache_dir=/tmp/mycache
```
**Code examples**: [`pytest.ini]`(pytest.ini)  
**Pytest docs**: [`full list of config options`](https://docs.pytest.org/en/stable/reference/reference.html#configuration-options)
___
[`pytest_addoption`](#contents)
-
Pytest hook used to parse passed command line arguments:
```
pytest test_file.py --arg=value
```
```python
# conftest.py
def pytest_addoption(parser):
  parser.addoption(
      "--arg",
      action="store",
      default="test",
      choises=("dev", "test", "stage")
      help="evironment to work with"
) 
```
**Code examples**: [`test_addoption.py`](tests/13_configuration/01_addoption/test_addoption.py)  
**Pytest docs**: [`about pytest_addoption`](https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=pytest_addoption#pytest.hookspec.pytest_addoption)  
___
[`pytest-dotenv`](#contents)
-
Pytest plugin used to load any `key=value` as environment variables from `.env` file. `.env` default file may be changed by another one or few in `pytest.ini` (or pass env by an argument `--envfile /path/to/.env`):
```ini
[pytest]
env_files=
  .users.dev.env
  .config.dev.env
```
**Code examples**: [`test_dotenv.py`](tests/13_configuration/02_dotenv/test_dotenv.py)
**Plugin docs**: [`about pytest-dotenv`](https://pypi.org/project/pytest-dotenv/)  
___
[`Logging levels`](#contents)
-
* Debug: Detailed information for debugging purposes.
* Info: General information about the program's execution.
* Warning: Potential issues or situations that may lead to errors.
* Error: Specific operation or functionality failure.
* Critical: Highest severity level for critical errors or failures.
___
[`CLI logs`](#contents)
-
Activated by setting the `log_cli` configuration option to true.
```ini
[pytest]
log_cli = True
log_level = DEBUG
log_format = %(asctime)s %(levelname)s %(message)s
log_date_format = %Y-%m-%d %H:%M:%S
```
Alternatively may be passed as an arguments `--log-cli-level`, `--log-cli-forma`, `--log-cli-date-format`.
**Code examples**: [`test_logging.py`](tests/12_logging/test_logging.py) [`pytest.ini`](tests/12_logging/pytest.ini)
**Pytest docs**: [`about CLI logs`](https://docs.pytest.org/en/stable/how-to/logging.html#live-logs)  
___
[`File logs`](#contents)
-
Activated by setting the `log_file` configuration option to true.
```ini
[pytest]
log_file = test.log
log_file_level = INFO
log_file_format = %(asctime)s %(levelname)s %(message)s
log_file_date_format = %Y-%m-%d %H:%M:%S
```
Alternatively may be passed as an arguments `--log-file-level`, `--log-file-forma`, `--log-file-date-format`.
**Code examples**: [`test_logging.py`](tests/12_logging/test_logging.py) [`pytest.ini`](tests/12_logging/pytest.ini)
**Pytest docs**: [`about file logs`](https://docs.pytest.org/en/stable/how-to/logging.html#live-logs)  
___
[`Fixture caplog`](#contents)
-
Inside the tests it is possible to change the log level for the captured log messages. This is supported by the caplog fixture:
```python
def test_logging(caplog):
    caplog.set_level(logging.INFO)
```
**Code examples**: [`test_logging.py`](tests/12_logging/test_logging.py) [`pytest.ini`](tests/12_logging/pytest.ini)  
**Pytest docs**: [`about caplog fixture`](https://docs.pytest.org/en/stable/how-to/logging.html#caplog-fixture)  
___
[`assertpy`](#contents)
-
Simple assertions library with fluent API. Provides assertions for strings, numbers, lists, tuples, dicts, sets, files, objects. Supports filtering and sorting
```python
from assertpy import assert_that

def test_something():
    assert_that(1 + 2).is_equal_to(3)
    assert_that('foobar').is_length(6).starts_with('foo').ends_with('bar')
    assert_that(['a', 'b', 'c']).contains('a').does_not_contain('x')
```
**Code examples**: [`test_01_assert_strings.py`](tests/14_plugins/01_assert/test_01_assert_strings.py) [`test_02_assert_numbers.py`](tests/14_plugins/01_assert/test_02_assert_numbers.py) [`test_03_assert_lists.py`](tests/14_plugins/01_assert/test_03_assert_lists.py) [`test_04_assert_tuples.py`](tests/14_plugins/01_assert/test_04_assert_tuples.py) [`test_05_assert_dicts.py`](tests/14_plugins/01_assert/test_05_assert_dicts.py) [`test_06_assert_sets.py`](tests/14_plugins/01_assert/test_06_assert_sets.py) [`test_07_assert_dates.py`](tests/14_plugins/01_assert/test_07_assert_dates.py) [`test_08_assert_files.py`](tests/14_plugins/01_assert/test_08_assert_files.py) [`test_09_assert_objects.py`](tests/14_plugins/01_assert/test_09_assert_objects.py) [`test_10_assert_filtering.py`](tests/14_plugins/01_assert/test_10_assert_filtering.py) [`test_10_assert_sorting.py`](tests/14_plugins/01_assert/test_11_assert_sorting.py)  
**Plugin docs**: [`plugin page`](https://pypi.org/project/assertpy/) [`full documentation on github`](https://github.com/assertpy/assertpy)  
___
[`pytest-rerunfailures`](#contents)
-
Re-run tests plugin to eliminate flaky failures. Provides CLI options to re-run all failed tests and decorator to re-run single flaky test.
#### CLI options to re-run all failed tests
```
# Re-run all failures
pytest --reruns 5

# Re-run all failures with 1 sec between re-runs
pytest --reruns 5 --reruns-delay 1

# Re-run all failures matching certain expressions
pytest --reruns 5 --only-rerun AssertionError
pytest --reruns 5 --only-rerun AssertionError --only-rerun ValueError

# Re-run all failures other than matching certain expressions
pytest --reruns 5 --rerun-except AssertionError
pytest --reruns 5 --rerun-except AssertionError --rerun-except OSError
```
#### Decorator to re-run single flaky test
```python
# Re-run individual failures. "reruns_delay" and "condition" are optional
@pytest.mark.flaky(reruns=5, reruns_delay=2, condition=sys.platform.startswith("win32"))
def test_example():
    import random
    assert random.choice([True, False])
```
**Code examples**: [`test_rerun.py`](tests/14_plugins/02_rerun/test_rerun.py)  
**Plugin docs**: [`plugin page with documentation`](https://pypi.org/project/pytest-rerunfailures/)  
___
[`pytest-xdist`](#contents)
-
The pytest-xdist plugin extends pytest with new test execution modes, the most used being distributing tests across multiple CPUs to speed up test execution.
#### Running tests across multiple CPUs
To send tests to multiple CPUs, use the -n (or --numprocesses) option:
```
# running in 3 processes:
pytest -n 3

# running as many processes as computer has CPU cores:
pytest -n auto
```
#### The test distribution algorithm is configured with the `--dist` CLI option
* `--dist` (default): Sends pending tests to any worker that is available, without any guaranteed order. Scheduling can be fine-tuned with the –maxschedchunk option, see output of pytest –help.
* `--dist` loadscope: Tests are grouped by module for test functions and by class for test methods. Groups are distributed to available workers as whole units. This guarantees that all tests in a group run in the same process. This can be useful if you have expensive module-level or class-level fixtures. Grouping by class takes priority over grouping by module.
* `--dist` loadfile: Tests are grouped by their containing file. Groups are distributed to available workers as whole units. This guarantees that all tests in a file run in the same worker.
* `--dist` loadgroup: Tests are grouped by the xdist_group mark. Groups are distributed to available workers as whole units. This guarantees that all tests with same xdist_group name run in the same worker. Example: `@pytest.mark.xdist_group(name="group1")`
**Code examples**: [`test_01_parallel_load_default.py`](tests/14_plugins/03_parallel/test_01_parallel_load_default.py) [`test_02_parallel_load_scope.py`](tests/14_plugins/03_parallel/test_02_parallel_load_scope.py) [`test_03_parallel_load_file.py`](tests/14_plugins/03_parallel/test_03_parallel_load_file.py) [`test_04_parallel_load_group.py`](tests/14_plugins/03_parallel/test_04_parallel_load_group.py) [`test_05_parallel_log_workers.py`](tests/14_plugins/03_parallel/05_log_workers/test_05_parallel_log_workers.py) [`test_06_parallel_fixture.py`](tests/14_plugins/03_parallel/06_single_session_scope_fixture/test_06_parallel_fixture.py)  
**Plugin docs**: [`plugin page`](https://pypi.org/project/pytest-xdist/) [`full documentation page`](https://pytest-xdist.readthedocs.io)  
