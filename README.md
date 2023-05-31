Pytest
=


Contents
-
**&nbsp;&nbsp;&nbsp;** **1. Conventions:** **&nbsp;** **[`Naming convention`](#naming-convention)**__,__ **[`Test discovery`](#test-discovery)**__.__  
**&nbsp;&nbsp;&nbsp;** **2. Test execution:** **&nbsp;** **[`Run tests`](#run-tests)**__,__ **[`Deselecting tests`](#deselecting-tests)**__,__ **[`Re-run tests`](#re-run-tests)**__,__ **[`CLI flags`](#cli-flags)**__.__  
**&nbsp;&nbsp;&nbsp;** **3. Fixtures:** **&nbsp;**  **[`What is fixture`](#what-is-fixture)**__,__**[`conftest.py`](#conftestpy)**__,__ **[`Fixtures scope`](#fixtures-scope)**__,__ **[`Autouse fixtures`](#autouse-fixtures)**__,__ **[`Fixtures order`](#fixtures-order)**__,__ **[`Built-in fixtures`](#built-in-fixtures)**__,__ **[`yield fixtures`](#combinatorics)**__.__  
**&nbsp;&nbsp;&nbsp;** **4. Marks:** **&nbsp;**  **[`skip`](#skip-mark)**__,__ **[`skipif`](#skipif-mark)**__,__ **[`xfail mark`](#xfail-mark)**__,__ **[`usefixtures mark`](#usefixtures-mark)**__,__ **[`Registering marks`](#registering-marks)**__.__  
**&nbsp;&nbsp;&nbsp;** **5. Parametrization:** **&nbsp;**  **[`Parametrize mark`](#parametrize-mark)**__,__ **[`Fixture parametrization`](#fixture-parametrization)**__,__ **[`pytest_generate_tests`](#pytestgeneratetests)**__,__ **[`Parametrization with marks`](#parametrization-with-marks)**__,__ **[`Indirect parametrization`](#indirect-parametrization)**__,__ **[`Parametrization scope`](#parametrization-scope)**__.__  
**&nbsp;&nbsp;&nbsp;** **6. Configuration:** **&nbsp;**  **[`pytest.ini`](#pytestini)**__,__ **[`pytest_addoption`](#pytestaddoption)**__,__ **[`pytest-dotenv`](#pytest-dotenv)**__.__  
**&nbsp;&nbsp;&nbsp;** **7. Logging:** **&nbsp;**  **[`Logging levels`](#logging-levels)**__,__ **[`CLI logs`](#cli-logs)**__,__ **[`File logs`](#file-logs)**__,__ **[`Fixture caplog`](#fixture-caplog)**__.__  
**&nbsp;&nbsp;&nbsp;** **8. Libs and plugins:** **&nbsp;**  **[`assertpy`](#assertpy)**__,__ **[`pytest-rerunfailures`](#pytest-rerunfailures)**__,__ **[`pytest-xdist`](#pytest-xdist)**__.__  

___
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
-
Pytest search for the tests from current directory based on [`Naming convention`](#naming-convention). Directory with tests may be specified in `pytest.ini` configuration file.  
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
### Prevent discovering specific Test classes
To prevent pytest from discovering classes that start with `Test` by setting a boolean `__test__` attribute to `False`:
```python
# Will not be discovered as a test
class TestClass:
    __test__ = False
```
### Avoiding file name collisions
Given next directory structure
```
dups
├── a
│   └── test_foo.py
└── b
    └── test_foo.py
```
Pytest will raise an error if both files are collected to run.  

Options to fix:
* use unique file names
  ```
  dups
  ├── a
  │   └── test_foo_a.py
  └── b
      └── test_foo_b.py
  ```
* add `__init__.py` to have python packages instead of directories
  ```
  dups_fixed/
  ├── a
  │   ├── __init__.py
  │   └── test_foo.py
  └── b
      ├── __init__.py
      └── test_foo.py
  ```
___
[`Run tests`](#contents)
---------
### Run tests in a module 
```bash
pytest tests/01_basic/test_naming.py
```
### Run tests in a directory 
```bash
pytest tests/01_basic/
```
### Run tests by keyword expressions
This will run tests which contain names that match the given string expression (case-insensitive), which can include Python operators that use filenames, class names and function names as variables.
```bash
pytest -k test_multiplication
```
```bash
pytest -k TestNamingClass
```
```bash
pytest -k test_naming.py
```
### Run tests by node ids
Each collected test is assigned a unique nodeid which consist of the module filename followed by specifiers like class names, function names and parameters from parametrization, separated by `::` characters.
```bash
pytest tests/01_basic/test_naming.py::test_multiplication
```
```bash
pytest tests/01_basic/test_class_naming.py::TestNamingClass::test_class_multiplication
```
### Run tests by marker expressions
Will run all tests which are decorated by a mark. For example, with the `@pytest.mark.slow` mark.
```bash
pytest -m slow
```
**Pytest docs**: [`Specifying which tests to run`](https://docs.pytest.org/en/stable/how-to/usage.html#specifying-which-tests-to-run)  
___
[`Deselecting tests`](#contents)
-
### Ignore paths during test collection
Ignore certain test directories and modules during collection by passing the `--ignore=path` option on the cli. Pytest allows multiple `--ignore` options.
```
pytest tests/01_basic --ignore=tests/01_basic/test_class_naming.py
pytest tests/01_basic --ignore=tests/01_basic/subdir
```
### Ignore test file paths based on Unix shell-style wildcards
The `--ignore-glob` option allows to ignore test file paths.
```
pytest tests/01_basic --ignore-glob='*class*'
pytest tests/01_basic --ignore-glob="./*subdir/"
pytest tests/01_basic --ignore-glob="./*subdir/" --ignore-glob="*class*"
```
### Deselect tests during test collection
Tests can individually be deselected during collection by passing the `--deselect=item` option. Pytest allows multiple `--deselect` options.
```
pytest tests/01_basic/subdir --deselect=tests/01_basic/subdir/test_in_subdir.py::test_two_in_subdir
pytest tests/01_basic --deselect=tests/01_basic/test_class_naming.py
pytest tests/01_basic --deselect=tests/01_basic/subdir
```
### Deselect tests by keyword expressions
This will run tests which contain names that match the given string expression (case-insensitive), which can include Python operators that use filenames, class names and function names as variables.
```
pytest -k "test_naming.py and not test_addition"
pytest -k "test_class_naming.py and not test_class_multiplication"
```
### Deselect based on mark
Marked tests may be deselected with `-m` option
```
pytest tests/01_basic -m "not slow"
```
**Pytest docs**: 
[`Deselecting paths and tests`](https://docs.pytest.org/en/7.3.x/example/pythoncollection.html)  
___
[`Re-run tests`](#contents)
-
### Re-run last failed tests only
```
pytest --lf, --last-failed 
```
### Re-run all tests, starting with last failed
```
pytest --ff, --failed-first
```
### Stepwise (runs until the first failure and then stop; next time continue from first failed)
```
pytest --sw, --stepwise
```
### Stepwise skip (ignores one failing test and stop test execution on the second failing test)
```
pytest --sw-skip, --stepwise-skip
```
### Clearing cache content (removes all cache contents at start of test run)
```
pytest --cache-clear
```
### Show cache content
```
pytest --cache-show
```
**Pytest docs**: 
[`how to re-run failed tests`](https://docs.pytest.org/en/stable/how-to/cache.html#how-to-re-run-failed-tests-and-maintain-state-between-test-runs)  
___
[`CLI flags`](#contents)
-
### Prints options and config file settings
```bash
pytest -h 
```
### Increase verbosity (more detailed output)
```
pytest -v, --verbose
```
### Decrease verbosity
```
pytest -q, --quite
```
### Disable stdout capturing (prints shown in console)
```
pytest -s, --capture=no
```
### Stop at first failure
```
pytest -x, --exitfirst
```
### Collect tests without execution
```
pytest --collect-only
```
### Show N slowest tests (N=0 for all)
```
pytest --durations=N
```
### JUnitXML format files (can be read by Jenkins or other CI/CD tool):
```
pytest --junit-xml=path
```
**Pytest docs**: [`full list of command-line-flags`](https://docs.pytest.org/en/stable/reference/reference.html#command-line-flags)
___
[`What is fixture`](#contents)
-
### Purpose of fixture
* Provides a defined, reliable and consistent context for the tests
* Is a function decorated with @pytest.fixture
* Used to design preconditions and postconditions
* Can be reused over tests
* Multiple fixtures may be used for test
* Sharing test data between tests
### Fixture example
```python
@pytest.fixture
def message():
    return 'fixture content'

@pytest.fixture(name='lue')  # fixture name may be shortened using 'name' param
def ultimate_answer_to_life_the_universe_and_everything():
    return 42

def test_has_fixture(message, lue):
    assert message == 'fixture content'
    assert lue == 42
```
### Fixture flags
```
# Show what fixtures and tests would be executed but don't execute anything
pytest tests/02_fixtures/test_simple_fixture.py --setup-plan

# Only setup fixtures, do not execute tests
pytest tests/02_fixtures/test_simple_fixture.py --setup-only

# Show setup of fixtures while executing tests
pytest tests/02_fixtures/test_simple_fixture.py --setup-show
```
**Code examples**: 
[`test_simple_fixture.py`](tests/02_fixtures/test_simple_fixture.py) 
[`test_inherited_fixture.py`](tests/03_fixtures_inherited/test_inherited_fixture.py)  
**Pytest docs**: 
[`about fixtures`](https://docs.pytest.org/en/stable/explanation/fixtures.html#about-fixtures)  
___
[`conftest.py`](#contents)
-
### Purpose of conftest
* Serves as a means of providing fixtures for an entire directory
* No need to do import for any test in same package
* Multiple conftest.py may be used as for root and sub-directories
* Defined fixtures may be overwritten in sub-directories
### Conftest flags
```
# Only load conftest.py's relative to specified dir
pytest tests/04_conftest/subdir/test_subdir_conftest.py --confcutdir=tests/04_conftest/subdir

# Don't load any conftest.py files
pytest tests/04_conftest --noconftest
```
**Code examples**: 
[`test_conftest.py`](tests/04_conftest/test_conftest.py) 
[`test_subdir_conftest.py`](tests/04_conftest/subdir/test_subdir_conftest.py)  
**Pytest docs**: 
[`about conftest.py`](https://docs.pytest.org/en/stable/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files)  
___
[`Fixtures scope`](#contents)
-
* function - the default scope, the fixture is destroyed at the end of the test
* class - the fixture is destroyed during teardown of the last test in the class
* module - the fixture is destroyed during teardown of the last test in the module
* package - the fixture is destroyed during teardown of the last test in the package
* session - the fixture is destroyed at the end of the test session
```
@pytest.fixture(scope='session')
def session_scope_fixture():
  return 'content of session scope feature'
```
**Code examples**: 
[`fixtures scope tests`](tests/05_fixtures_scope)  
**Pytest docs**: 
[`about fixtures scope`](https://docs.pytest.org/en/stable/how-to/fixtures.html#fixture-scopes)  
___
[`Autouse fixtures`](#contents)
-
* Convenient way to make all tests automatically request fixture
* Cut out a lot of redundant requests
* Provide more advanced fixture usage
* autouse=True makes a fixture configured for autouse
```python
@pytest.fixture(autouse=True)
def auto_used_fixture():
    return 'auto used feature content'
```
**Code examples**: 
[`test_autouse_fixtures.py`](tests/06_autouse_fixtures/test_autouse_fixtures.py)  
**Pytest docs**: 
[`about autouse fixtures`](https://docs.pytest.org/en/stable/how-to/fixtures.html#autouse-fixtures-fixtures-you-don-t-have-to-request)  
___
[`Fixtures order`](#contents)
-
* Based on 3 factors:
  * scope
  * dependencies
  * autouse
* Higher-scoped fixtures are executed first. Higher-scopes (such as session) are executed before lower-scoped fixtures (such as function or class)
  ```python
    @pytest.fixture()
    def runs_second():
        pass
  
  
    @pytest.fixture(scope='session')
    def runs_first():
        pass
  ```
* Fixtures of the same order execute based on dependencies
  ```python
    @pytest.fixture()
    def runs_second(runs_first):
        pass

    @pytest.fixture()
    def runs_first():
        pass
  ```
* Autouse fixtures are executed first within their scope
    ```python
    @pytest.fixture()
    def runs_second():
        pass
  
  
    @pytest.fixture(autouse=True)
    def runs_first():
        pass
  ```

**Code examples**: 
[`test_fixtures_order.py`](tests/07_fixtures_order/test_fixtures_order.py)  
**Pytest docs**: 
[`about fixtures order`](https://docs.pytest.org/en/stable/reference/fixtures.html#fixture-instantiation-order)  
___
[`Built-in fixtures`](#contents)
-
### tmp_path and tmp_path_factory
* tmp_path temporary directory unique to the test invocation. 
  ```python
  def test_tmp_path_fixture(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text('text content')
    assert p.read_text() == 'text content'
  ```
* tmp_path_factory is a session-scope fixture provides temporary directory during all test run.
  ```python
  @pytest.fixture(scope="session")
  def data_file(tmp_path_factory):
    temp_dir = tmp_path_factory.mktemp("data")
    temp_file = temp_dir / "example.txt"
    temp_file.write_text('text content')
    return temp_file
  
  def test_tmp_path_factory_fixture(data_file):
    assert 'text content' == data_file.read_text()
  ```
* fixtures configuration in pytest.ini
  ```ini
  [pytest]
  ;set how many sessions should we keep the tmp_path directories (default 3)
  tmp_path_retention_count = 5
  
  ;control which directories created by the tmp_path fixture are kept around, based on test outcome (default all)
  ;  * all: retains directories for all tests, regardless of the outcome
  ;  * failed: retains directories only for tests with outcome error or failed
  ;  * none: directories are always removed after each test ends, regardless of the outcome
  tmp_path_retention_policy = "failed"
  ```
**Code examples**:
[`test_01_tmp_path.py`](tests/08_built_in_fixtures/01_temp_directory/test_01_tmp_path.py) 
[`test_02_tmp_path_factory.py`](tests/08_built_in_fixtures/01_temp_directory/test_02_tmp_path_factory.py)  
**Pytest docs**: 
[`tmp_path`](https://docs.pytest.org/en/stable/how-to/tmp_path.html#the-tmp-path-fixture) and [`tmp_path_factory`](https://docs.pytest.org/en/stable/how-to/tmp_path.html#the-tmp-path-factory-fixture)
### request
Provide information on the executing test function such as passed arguments, pytest configuration, fixtures etc.  
* `request.node.nodeid`  
  Test id, i.e. `tests/path/test_request_fixture.py::test_request`.
* `request.path`  
  Provides path to test file, i.e. `tests/path/test_request_fixture.py`.
* `request.fixturenames`  
  List all used fixtures.
* `request.config.getini('addopts')`  
  Get configuration parameter value from `pytest.ini`. 
* `request.config.getoption('--option-name')`  
  Get CLI option value. Has additional test policy on missing option and default value:
  ```python
  def test_request_fixture_skip_by_missing_option(request: pytest.FixtureRequest):
    assert request.config.getoption('missing_option', skip=True) == 'will skip'

  def test_request_fixture_default_option(request: pytest.FixtureRequest):
    assert request.config.getoption('default_option', default='default_value') == 'default_value'

  def test_request_fixture_passed_option(request: pytest.FixtureRequest):
    assert request.config.getoption('-s') == 'no'
  ```
**Code examples**: 
[`test_request_fixture.py`](tests/08_built_in_fixtures/02_request/test_request_fixture.py)  
**Pytest docs**: 
[`request`](https://docs.pytest.org/en/stable/reference/reference.html#request)  
### monkeypatch
Has helper methods for safely patching and mocking functionality in tests. Change current directory, update environment variables, mock objects. All modifications not affecting original environment. Modifications relates to test execution only. 
```python
monkeypatch.setattr(obj, name, value, raising=True)
monkeypatch.delattr(obj, name, raising=True)
monkeypatch.setitem(mapping, name, value)
monkeypatch.delitem(obj, name, raising=True)
monkeypatch.setenv(name, value, prepend=None)
monkeypatch.delenv(name, raising=True)
monkeypatch.syspath_prepend(path)
monkeypatch.chdir(path)
monkeypatch.context()
```
All modifications will be undone after the requesting test function or fixture has finished. The raising parameter determines if a KeyError or AttributeError will be raised if the target of the set/deletion operation does not exist.
* Modify `sys.path`  
  Prepend the path to `sys.path`, allowing Python to locate and import the custom module. This is useful when need to test code that depends on external modules or libraries.
  ```python
  def test_syspath_prepend(monkeypatch):
    new_path = "/path/to/my/module"
    monkeypatch.syspath_prepend(new_path)
  
    import new_module
    # perform actions with imported module
  ```
* Change working directory  
  `monkeypatch.chdir` method changes the current working directory to the specified path. helpful when need to test code that depends on the current working directory (CWD).
  ```python
  def test_chdir(monkeypatch):
    monkeypatch.chdir('/my/custom/path')
    assert os.getcwd() == '/my/custom/path'
  ```
* Modify dictionaries  
  Modifying the values of dictionaries e.g. any global configuration can be modified for certain test cases. Use `monkeypatch.setitem` to patch the dictionary for the test. `monkeypatch.delitem` can be used to remove items. If raising is set to True (default), it raises an exception if the item does not exist.
  ```python
  CONFIG = {'key1': 'value1', 'key2': 'value2'}

  def test_setitem(monkeypatch):
      monkeypatch.setitem(CONFIG, 'key1', 'new_value')
      assert CONFIG['key1'] == 'new_value'
  
  def test_delitem(monkeypatch):
      monkeypatch.delitem(CONFIG, 'key2')
      assert 'key2' not in CONFIG
  ```
* Modify environment variables
  Manipulate environment variables for a test. Add/update/delete variable or prepend values to existing environment variable.
  ```python
  def test_monkey_update_env(monkey_user):
    # overwrite existing USER environment variable:
    monkeypatch.setenv("USER", "testinguser")
    assert os.getenv("USER") == "testinguser"

  def test_monkey_new_env(monkeypatch):
      assert 'MY_PARAM' not in os.environ
      # create new environment variable:
      monkeypatch.setenv("MY_PARAM", "my variable")
      assert os.getenv("MY_PARAM") == "my variable"

  def test_monkey_prepend(monkeypatch, tmp_path):
      initial_paths_count = len(os.getenv('PATH').split(":"))
      # add value to environment variable:
      monkeypatch.setenv("PATH", str(tmp_path), prepend=":")
      paths = os.getenv('PATH').split(":")
      assert len(paths) == initial_paths_count + 1
      assert paths[0] == str(tmp_path)
  
  def test_monkey_delete_env(monkeypatch):
      assert 'HOME' in os.environ
      monkeypatch.delenv("HOME")
      assert 'HOME' not in os.environ
  
  def test_monkey_delete_env_raises(monkeypatch):
      assert 'MY_PARAM' not in os.environ
      with pytest.raises(KeyError):
          monkeypatch.delenv("MY_PARAM", raising=True)
  ```
* Modify attributes
  Methods `monkeypatch.setattr`, `monkeypatch.delattr` sets/deletes the attribute of an object. If the attribute does not exist, it can optionally raise an AttributeError.
  ```python
  def test_context(monkeypatch, tmp_path):
    initial_wd = os.getcwd()
    with monkeypatch.context() as monkey:  # context mocks works only under its code block
        monkey.setattr(os, "getcwd", lambda: str(tmp_path))
        assert os.getcwd() == str(tmp_path)
    assert os.getcwd() == initial_wd


  def test_undo(monkeypatch, tmp_path):
      monkeypatch.delattr("os.getcwd")
      with pytest.raises(AttributeError):
          print(os.getcwd())
      monkeypatch.undo()  # undo previous monkeypatch
      print(os.getcwd())
  ```
**Code examples**: 
[`test_monkeypatch_attributes.py`](tests/08_built_in_fixtures/03_mokeypatch/test_monkeypatch_attributes.py)
[`test_monkeypatch_attributes_path.py`](tests/08_built_in_fixtures/03_mokeypatch/test_monkeypatch_attributes_path.py)
[`test_monkeypatch_attributes_request.py`](tests/08_built_in_fixtures/03_mokeypatch/test_monkeypatch_attributes_request.py)
[`test_monkeypatch_change_working_directory.py`](tests/08_built_in_fixtures/03_mokeypatch/test_monkeypatch_change_working_directory.py)
[`test_monkeypatch_dictionaries.py`](tests/08_built_in_fixtures/03_mokeypatch/test_monkeypatch_dictionaries.py)
[`test_monkeypatch_environment_variables.py`](tests/08_built_in_fixtures/03_mokeypatch/test_monkeypatch_environment_variables.py)
[`test_monkeypatch_syspath_prepend.py`](tests/08_built_in_fixtures/03_mokeypatch/test_monkeypatch_syspath_prepend.py)
[`test_monkeypatch_context.py`](tests/08_built_in_fixtures/03_mokeypatch/test_monkeypatch_context.py)
**Pytest docs**: 
[`monkeypatch`](https://docs.pytest.org/en/stable/how-to/monkeypatch.html)  
### cache
Stores values in pytest cache and retrieve values across test runs. 

For example, any expensive computation may be cached once evaluated. Next test run evaluated data is able from cache to get:
```python
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
```
Works with data that is JSON serializable:
* works with examples:
  * `cache.set("key", "42")`
  * `cache.set("key", [1, 2, 3])`
  * `cache.set("key", {"name": "John", "age": 30})`
* TypeError caused on examples:
  * `cache.set("key", int)`
  * `cache.set("my_data", set([1, 2, 3]))`
  * `cache.set("my_data", file_obj)`

**Code examples**: 
[`test_config_cache.py`](tests/08_built_in_fixtures/04_config_cache/test_config_cache.py)  
**Pytest docs**: 
[`cache`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-cache)  
### and other built-in fixtures...
Capture output or logs; record extra properties; record warnings etc.
**Pytest docs**: 
[`built-in fixtures`](https://docs.pytest.org/en/stable/reference/fixtures.html#built-in-fixtures)
___
[`yield fixtures`](#contents)
-
* `return` is swapped out for `yield`
* Any teardown code for that fixture is placed after the yield
* Once the test is finished, pytest will go back down the list of fixtures, but in the reverse order, taking each one that yielded, and running the code inside it that was after the yield statement.
```python
@pytest.fixture
def mail_box():
    # setup/preconditions:
    box = MailBox()
    yield box
    # teardown/postconditions:
    box.clear()
```
**Code examples**: 
[`test_yield_fixture.py`](tests/09_yield_fixtures/test_yield_fixture.py)  
**Pytest docs**: 
[`about yield fixtures`](https://docs.pytest.org/en/stable/how-to/fixtures.html#yield-fixtures-recommended)
___
[`skip mark`](#contents)
-
The simplest way to skip a test function is to mark it with the skip decorator which may be passed an optional reason. However, there are several approaches for the test to be skipped.
### Mark the test with `@pytest.mark.skip("reason is optional")`
```python
@pytest.mark.skip(reason="requirements changes CHN-123")
def test_with_skip_mark():
```
### Mark the test with defined mark
```python
integration_needed = pytest.mark.skip("cannot be done without integration")

@integration_needed
def test_skip_by_defined_marker():
```
### Mark the test with imported mark
```python
# content of markers.py:
req_change_skip = pytest.mark.skip("requirements changed")

# content of test file:
import markers
@markers.req_change_skip
def test_skip_by_imported_marker():
```
### Skip all tests in module by defining global variable pytestmark
```python
pytestmark = pytest.mark.skip("removed from requirements")
```
### Skip imperatively by `pytest.skip` function
```python
def test_skip_with_pytest_skip():
    if not valid_config():
        pytest.skip("unsupported configuration")
```
### Skip imperatively all module by `pytest.skip` function
```python
if not sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)
```
### Skip imperatively from fixture by `pytest.skip` function
```python
@pytest.fixture()
def setup(env):
    if env == "bad_env":
        pytest.skip("not running on bad env")
```
### Show extra information of skipped tests
```
pytest -rs
```
**Code examples**: 
[`test_skip.py`](tests/10_bult_in_marks/01_skip/test_skip.py) 
[`test_skip_defined_mark.py`](tests/10_bult_in_marks/01_skip/test_skip_defined_mark.py)
[`test_skip_defined_mark_outside.py`](tests/10_bult_in_marks/01_skip/test_skip_defined_mark_outside.py)
[`test_skip_all_test_in_module.py`](tests/10_bult_in_marks/01_skip/test_skip_all_test_in_module.py) 
[`test_skip_imperatively.py`](tests/10_bult_in_marks/01_skip/test_skip_imperatively.py) 
[`test_skip_imperatively_all_module.py`](tests/10_bult_in_marks/01_skip/test_skip_imperatively_all_module.py)  
[`test_skip_imperatively_from_fixture.py`](tests/10_bult_in_marks/01_skip/test_skip_imperatively_from_fixture.py)  
**Pytest docs**: 
[`about skip mark`](https://docs.pytest.org/en/stable/how-to/skipping.html#skipping-test-functions)  
___
[`skipif mark`](#contents)
-
Skip test conditionally. If the condition evaluates to `True` during collection, the test function will be skipped.  
### Mark the test with `@pytest.mark.skipif(<condition>, reason="reason is required")`
```python
@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10")
def test_with_skipif_mark():
```
### Mark the test with defined skipif mark
```python
min_version = pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")

@min_version
def test_skipif_by_defined_marker():
```
### Mark the test with imported skipif mark
```python
# content of filters.py:
min_version = pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")

# content of test file:
import filters
@filters.min_version
def test_skipif_by_imported_marker():
```
### Skip by condition all tests in module by defining global variable pytestmark
```python
pytestmark = pytest.mark.skipif(sys.platform == "win32", reason="tests for linux only")
```
**Code examples**: 
[`test_skipif.py`](tests/10_bult_in_marks/02_skipif/test_skipif.py) 
[`test_skipif_all_test_in_module.py`](tests/10_bult_in_marks/02_skipif/test_skipif_all_test_in_module.py) 
[`test_skipif_defined_mark.py`](tests/10_bult_in_marks/02_skipif/test_skipif_defined_mark.py) 
[`test_skipif_defined_mark_outside.py`](tests/10_bult_in_marks/02_skipif/test_skipif_defined_mark_outside.py) 
**Pytest docs**: 
[`about skipif mark`](https://docs.pytest.org/en/stable/how-to/skipping.html#id1)  
___
[`xfail mark`](#contents)
-
### The xfail marker indicates a test expect to fail
xfail means that test expect to fail for some reason. A common example is a test for a feature not yet implemented, or a bug not yet fixed. When a test passes despite being expected to fail (marked with `pytest.mark.xfail`), it’s an xpass and will be reported in the test summary.
```python
@pytest.mark.xfail()
def test_xfail_mark():
    pass
```
Alternatively, you can also mark a test as `XFAIL` from within the test or its setup function imperatively:
```python
def test_xfail_function():
    if not valid_config():
        pytest.xfail("failing configuration (but should work)")
```
### xfail reason parameter
Specify the reason of expected failure
```python
@pytest.mark.xfail(reason="BUG-123")
def test_xfail_reason():
    pass
```
### xfail condition parameter
If a test is only expected to fail under a certain condition, then it can set with the first parameter:
```python
@pytest.mark.xfail(sys.platform == "win32", reason="bug in a 3rd party library")
def test_xfail_condition():
    pass
```
### xfail raises parameter
If you want to be more specific as to why the test is failing, you can specify a single exception, or a tuple of exceptions, in the `raises` argument.
```python
@pytest.mark.xfail(raises=RuntimeError)
def test_xfail_raises():
    pass
```
### xfail run parameter
If a test should be marked as xfail and reported as such but should not be even executed, then `run` parameter should be used with `False` value:
```python
@pytest.mark.xfail(run=False)
def test_xfail_run():
    pass
```
### xfail strict parameter
Both `XFAIL` and `XPASS` don’t fail the test suite by default. This setting can be changed by setting the strict keyword-only parameter to True.
```python
@pytest.mark.xfail(strict=True)
def test_xfail_strict():
    pass
```
This will make `XPASS` (“unexpectedly passing”) results from this test to fail the test suite.
Parameter strict can be configured in pytest.ini:
```ini
xfail_strict=true
```
### xfail flag --runxfail
Force the running and reporting of an xfail marked test as if it weren’t marked at all. 
This also causes `pytest.xfail()` to produce no effect.
**Code examples**: 
[`test_xfail.py`](tests/10_bult_in_marks/03_xfail/test_xfail.py) 
[`test_xfail_condition.py`](tests/10_bult_in_marks/03_xfail/test_xfail_condition.py) 
[`test_xfail_ignore_mark.py`](tests/10_bult_in_marks/03_xfail/test_xfail_ignore_mark.py) 
[`test_xfail_no_run.py`](tests/10_bult_in_marks/03_xfail/test_xfail_no_run.py) 
[`test_xfail_strict.py`](tests/10_bult_in_marks/03_xfail/test_xfail_strict.py)  
**Pytest docs**: 
[`about xfail mark`](https://docs.pytest.org/en/stable/how-to/skipping.html#xfail-mark-test-functions-as-expected-to-fail)  
___
[`usefixtures mark`](#contents)
-
### Mark a test function as using the given fixture names
```python
@pytest.mark.usefixtures("perform_config")
def test_with_usefixtures_mark():
    pass
```
### Other options to use usefixtures
```
1. May specify fixture usage at the test module level using pytestmark:
    pytestmark = pytest.mark.usefixtures("precondition_one", "precondition_two")

2. It is also possible to put fixtures required by all tests in your project into pytest.ini:
    [pytest]
    usefixtures = precondition_one precondition_two
```
**Code examples**: 
[`test_usefixtures.py`](tests/10_bult_in_marks/04_usefixtures/test_usefixtures.py)  
**Pytest docs**: 
[`about usefixtures mark`](https://docs.pytest.org/en/stable/how-to/fixtures.html#usefixtures)  
___
[`Registering marks`](#contents)
-
#### Custom marks can be registered in pytest.ini file:
```ini
[pytest]
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    integration
```
#### Custom marks can be registered programmatically in a pytest_configure hook
```python
# conftest.py
def pytest_configure(config):
    config.addinivalue_line("markers", "slow: too slow test")
    config.addinivalue_line("markers", "integration: service integration")
```
**Pytest docs**: 
[`about registering marks`](https://docs.pytest.org/en/stable/how-to/mark.html#registering-marks)  
___
[`Parametrize mark`](#contents)
-
### Parametrize test
The builtin `pytest.mark.parametrize` decorator enables parametrization of arguments for a test function.
```python
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```
Parametrize marker parameters:
 * argnames - a comma-separated string denoting one or more argument names, or a list/tuple of argument strings.
 * argvalues - the list of values for each argument
 * ids - id for each argument includes in test name
```python
@pytest.mark.parametrize(
    argnames="test_input,expected",
    argvalues=[("3+5", 8), ("2+4", 6)],
    ids=["sum check: 3+5=8", "sum check: 2+4=6"]
)
def test_param_with_ids(test_input, expected):
    assert eval(test_input) == expected
```
Parametrize from dictionary:
```python
params = {
    "argnames": "test_input,expected",
    "argvalues": [("3+5", 8), ("2+4", 6)],
    "ids": ["sum check: 3+5=8", "sum check: 2+4=6"]
}

@pytest.mark.parametrize(**params)
def test_param_by_dict(test_input, expected):
    assert eval(test_input) == expected
```
### Parametrize module
Declaring `pytest.mark.parametrize` will parametrize all test functions and classes in given test file.
```python
pytestmark = pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
```
**Code examples**: 
[`test_parametrize_by_mark.py`](tests/11_parametrize/01_mark/test_parametrize_by_mark.py) 
[`test_parametrize_module_by_mark.py`](tests/11_parametrize/01_mark/test_parametrize_module_by_mark.py)  
**Pytest docs**: 
[`about @pytest.mark.parametrize`](https://docs.pytest.org/en/stable/how-to/parametrize.html#pytest-mark-parametrize-parametrizing-test-functions)  
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
**Code examples**: 
[`test_parametrize_by_fixture.py`](tests/11_parametrize/02_fixture/test_parametrize_by_fixture.py)  
**Pytest docs**: 
[`about fixture parametrization`](https://docs.pytest.org/en/stable/how-to/fixtures.html#fixture-parametrize)  
___
[`pytest_generate_tests`](#contents)
-
Pytest hook which is called when collecting a test function. Can be used to dynamically generate tests. For example based on command-line options:
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
  # if test using fixture then 
    if "stringinput" in metafunc.fixturenames: 
        metafunc.parametrize(argnames="stringinput", argvalues=metafunc.config.getoption("stringinput"))

# content of test file:
def test_parametrize_by_generate(stringinput):
    assert stringinput.isalpha()
```
**Code examples**: 
[`test_parametrize_by_generate.py`](tests/11_parametrize/03_generate/test_parametrize_by_generate.py)  
**Pytest docs**: 
[`about pytest_generate_tests`](https://docs.pytest.org/en/stable/how-to/parametrize.html#pytest-generate-tests)  
___
[`Parametrization with marks`](#contents)
-
Function `pytest.param()` can be set up with marks:
```python
@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (1, 2),
        pytest.param(1, 0, marks=[pytest.mark.xfail, pytest.mark.slow]),
        pytest.param(1, 3, marks=pytest.mark.xfail(reason="some bug")),
        pytest.param(
            10, 11, marks=pytest.mark.skipif(sys.version_info >= (3, 0), reason="py2k")
        ),
    ],
)
def test_increment(n, expected):
    assert n + 1 == expected
```
**Code examples**: 
[`test_marks_with_parametrize.py`](tests/11_parametrize/04_parametrize_with_marks/test_marks_with_parametrize.py)  
**Pytest docs**: 
[`parametrize mark`](https://docs.pytest.org/en/stable/how-to/parametrize.html)  
___
[`Indirect parametrization`](#contents)
-
### indirect=True
Using the indirect=True parameter when parametrizing a test allows to parametrize a test with a fixture receiving the values before passing them to a test:
```python
@pytest.fixture
def fixt(request):
    return request.param * 3

@pytest.mark.parametrize("fixt", ["a", "b"], indirect=True)
def test_indirect(fixt):
    assert len(fixt) == 3
```
This can be used, for example, to do more expensive setup at test run time in the fixture, rather than having to run those setup steps at collection time.
### Apply indirect on particular arguments
There is opportunity to apply indirect parameter on particular arguments. It can be done by passing list or tuple of arguments’ names to indirect  
```python
@pytest.fixture(scope="function")
def x(request):
    return request.param * 3


@pytest.fixture(scope="function")
def y(request):
    return request.param * 2


@pytest.mark.parametrize("x, y", [("a", "b")], indirect=["x"])
def test_indirect(x, y):
    assert x == "aaa"
    assert y == "b"
```
**Code examples**: 
[`test_indirect_01_true.py`](tests/11_parametrize/06_indirect/test_indirect_01_true.py) 
[`test_indirect_02_args.py`](tests/11_parametrize/06_indirect/test_indirect_02_args.py)    
**Pytest docs**: 
[`indirect parametrization docs`](https://docs.pytest.org/en/7.4.x/example/parametrize.html#indirect-parametrization)  
___
[`Parametrization scope`](#contents)
-
Denotes the scope of the parameters. The scope is used for grouping tests by parameter instances. It will also override any fixture-function defined scope, allowing to set a dynamic scope using test context or configuration.  

For example, with following `scope="class"`, fixtures called once per class and not by each function: 
```python
@pytest.fixture(scope="function")
def x(request):
    val = request.param[0] * 2
    return val

@pytest.mark.parametrize(argnames="x", argvalues=["a", "b"], indirect=True, scope="class")
class TestClass:
    def test_first_param_scope(self, x):
        assert len(x) == 2

    def test_second_param_scope(self, x):
        assert len(x) == 2
```
**Code examples**: 
[`test_parametrize_scope_01_mark.py`](tests/11_parametrize/scope/test_parametrize_scope_01_mark.py) 
[`test_parametrize_scope_02_hook.py`](tests/11_parametrize/scope/test_parametrize_scope_02_hook.py)  
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
Alternatively, may set a `PYTEST_ADDOPTS` environment variable to add command line options while the environment is in use:
```
export PYTEST_ADDOPTS="-v"
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
**Code examples**: 
[`pytest.ini`](pytest.ini)  
**Pytest docs**: 
[`full list of config options`](https://docs.pytest.org/en/stable/reference/reference.html#configuration-options)  
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
      choices=("dev", "test", "stage"),  # choices is optional
      help="evironment to work with"
) 
```
Note: Hook Session and test running activities will invoke all hooks defined in conftest.py files closer to the root of the filesystem.  

**Code examples**: 
[`test_addoption.py`](tests/12_configuration/01_addoption/test_addoption.py) 
[`conftest.py`](tests/12_configuration/01_addoption/conftest.py)  
**Pytest docs**: 
[`about pytest_addoption`](https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=pytest_addoption#pytest.hookspec.pytest_addoption)  
___
[`pytest-dotenv`](#contents)
-
### Install
```
pip3 install pytest-dotenv
```
### Basic usage
Pytest plugin used to load any `key=value` as environment variables from `.env` file. 
```properties
# .env default file
admin_username=dev_admin_name
admin_password=dev_admin_pswd
```
```python
@pytest.fixture(autouse=True)
def init():
    admin_username = os.environ["admin_username"]
    admin_password = os.environ["admin_password"]
```
### Custom environment 
`.env` default file may be changed by another one or few in `pytest.ini` (or pass env by an argument `--envfile /path/to/.env`):
```ini
[pytest]
env_files=
  .users.dev.env
  .config.dev.env
```
The files will be loaded and added to the os.environ dict object before any tests are run. If the files are not found on the working directory, it will search for the files in the ancestor directory and upwards.  
### Overriding existing values
By default the plugin will not override any variables already defined. To change behavior set env_override_existing_values in configuration
```ini
[pytest]
env_override_existing_values = 1
```
**Code examples**: 
[`test_dotenv.py`](tests/13_configuration/02_dotenv/test_dotenv.py)  
**Plugin docs**: 
[`about pytest-dotenv`](https://pypi.org/project/pytest-dotenv/)  
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
Activated by setting the `log_cli` configuration option to true. Also able to set logging level, message format and date format.
```ini
[pytest]
log_cli = True
log_level = DEBUG
log_format = %(asctime)s %(levelname)s %(message)s
log_date_format = %Y-%m-%d %H:%M:%S
```
Alternatively may be passed as an arguments 
  * `--log-cli-level` 
  * `--log-cli-format` 
  * `--log-cli-date-format`

**Code examples**: 
[`test_logging.py`](tests/13_logging/test_logging.py) 
[`pytest.ini`](tests/13_logging/pytest.ini)  
**Pytest docs**: 
[`about file logs`](https://docs.pytest.org/en/stable/how-to/logging.html#live-logs)  
**Python docs**: 
[`about logging`](https://docs.python.org/3/library/logging.html)  
___
[`File logs`](#contents)
-
Activated by adding the `log_file` configuration option. Also able to set logging level, message format and date format.
```ini
[pytest]
log_file = test.log
log_file_level = INFO
log_file_format = %(asctime)s %(levelname)s %(message)s
log_file_date_format = %Y-%m-%d %H:%M:%S
```
Alternatively may be passed as an arguments:
 * `--log-file`
 * `--log-file-level` 
 * `--log-file-format` 
 * `--log-file-date-format`

**Code examples**: 
[`test_logging.py`](tests/13_logging/test_logging.py) 
[`pytest.ini`](tests/13_logging/pytest.ini)  
**Pytest docs**: 
[`about file logs`](https://docs.pytest.org/en/stable/how-to/logging.html#live-logs)  
**Python docs**: 
[`about logging`](https://docs.python.org/3/library/logging.html)  
___
[`Fixture caplog`](#contents)
-
Inside the tests or fixtures it is possible to change the log level for the captured log messages. This is supported by the caplog fixture:
```python
def test_logging(caplog):
    caplog.set_level(logging.INFO)
    logging.debug("Ignored message")  # DEBUG ignored due to logging level set to INFO
```
**Code examples**: 
[`test_logging.py`](tests/13_logging/test_logging.py) 
[`pytest.ini`](tests/13_logging/pytest.ini)  
**Pytest docs**: 
[`about caplog fixture`](https://docs.pytest.org/en/stable/how-to/logging.html#caplog-fixture)  
___
[`assertpy`](#contents)
-
Simple assertions library with fluent API. Provides assertions for strings, numbers, lists, tuples, dicts, sets, files, objects. Supports filtering and sorting.
### Asserting strings
```python
from assertpy import assert_that

def test_with_assert_that():
    assert_that(1 + 2).is_equal_to(3)
    assert_that('foobar').is_length(6).starts_with('foo').ends_with('bar')
    assert_that(['a', 'b', 'c']).contains('a').does_not_contain('x')
```
### Asserting numbers
```python 
    assert_that(123).is_greater_than(100)
    assert_that(123).is_less_than_or_equal_to(200)
    assert_that(123).is_between(100, 200)
    assert_that(123).is_close_to(100, 25)
 ```
### Asserting lists
```python
    assert_that(['a', 'b']).contains('b', 'a')
    assert_that(['c', 'b', 'a']).is_sorted(reverse=True)
    assert_that(['a', 'b', 'c']).does_not_contain_duplicates()
```
### Asserting tuples
```python
    assert_that((1, 2, 3)).contains(3, 2, 1)
    assert_that((1, 2, 3)).does_not_contain(4, 5, 6)
    assert_that((1, 2, 3)).contains_only(1, 2, 3)
    assert_that((1, 2, 3)).is_sorted()
```
### Asserting dicts
```python
    assert_that({'a': 1, 'b': 2}).is_equal_to({'b': 2, 'a': 1})
    assert_that({'a': 1, 'b': 2}).contains_only('a', 'b')
    assert_that({'a': 1, 'b': 2}).is_subset_of({'a': 1, 'b': 2, 'c': 3})
    assert_that({'a': 1, 'b': 2}).contains_value(1)
    assert_that({'a': 1, 'b': 2}).contains_entry({'a': 1})
``` 
### Asserting sets
```python
    assert_that(set(['a', 'b'])).is_equal_to(set(['b', 'a']))
    assert_that(set(['a', 'b'])).does_not_contain('x', 'y')
    assert_that(set(['a', 'b'])).is_subset_of(set(['a', 'b', 'c']))
```
### Asserting dates
```python
    today = datetime.datetime.today()
    yesterday = today - datetime.timedelta(days=1)

    assert_that(yesterday).is_before(today)
    assert_that(today).is_after(yesterday)

    middle = today - datetime.timedelta(hours=12)
    assert_that(middle).is_between(yesterday, today)
  
    today_0h = today - datetime.timedelta(hours=today.hour)
    assert_that(today).is_equal_to_ignoring_time(today_0h)
  
    x = datetime.datetime(1980, 1, 2, 3, 4, 5, 6)  # 1980-01-02 03:04:05.000006
    assert_that(x).has_month(1)
```
### Asserting files
```python
    assert_that('foo.txt').exists()
    assert_that('foo.txt').is_file()
    assert_that('test_dir').is_directory()
    contents = contents_of('foo.txt', 'ascii')
    assert_that(contents).starts_with('foo').ends_with('bar').contains('oob')
```
### Asserting objects
```python
    fred = Person('Fred', 'Smith')
    bob = Person('Bob', 'Barr')
    people = [fred, bob]

    # first_name is a class attribute
    assert_that(people).extracting('first_name').is_equal_to(['Fred', 'Bob'])
    assert_that(people).extracting('first_name').contains('Fred', 'Bob')
    assert_that(people).extracting('first_name').does_not_contain('Charlie')
```   
### Assert filtering
```python
    users = [
        {'user': 'Fred', 'age': 36, 'active': True},
        {'user': 'Bob', 'age': 40, 'active': False},
        {'user': 'Johnny', 'age': 13, 'active': True}
    ]
    assert_that(users).extracting('user', filter='active').is_equal_to(['Fred', 'Johnny'])
    assert_that(users).extracting('user', filter={'age': 36, 'active': True}).is_equal_to(['Fred'])
    assert_that(users).extracting('user', filter=lambda x: x['age'] > 20).is_equal_to(['Fred', 'Bob'])
```
### Assert sorting
```python
    users = [
        {'user': 'Fred', 'age': 36, 'active': True},
        {'user': 'Bob', 'age': 40, 'active': False},
        {'user': 'Johnny', 'age': 13, 'active': True}
    ]
    assert_that(users).extracting('user', sort='age').is_equal_to(['Johnny', 'Fred', 'Bob'])
    assert_that(users).extracting('user', sort=['active', 'age']).is_equal_to(['Bob', 'Johnny', 'Fred'])
    assert_that(users).extracting('user', sort=lambda x: -x['age']).is_equal_to(['Bob', 'Fred', 'Johnny'])
```
**Code examples**: 
[`test_01_assert_strings.py`](tests/14_plugins/01_assert/test_01_assert_strings.py) 
[`test_02_assert_numbers.py`](tests/14_plugins/01_assert/test_02_assert_numbers.py)
[`test_03_assert_lists.py`](tests/14_plugins/01_assert/test_03_assert_lists.py) 
[`test_04_assert_tuples.py`](tests/14_plugins/01_assert/test_04_assert_tuples.py) 
[`test_05_assert_dicts.py`](tests/14_plugins/01_assert/test_05_assert_dicts.py) 
[`test_06_assert_sets.py`](tests/14_plugins/01_assert/test_06_assert_sets.py) 
[`test_07_assert_dates.py`](tests/14_plugins/01_assert/test_07_assert_dates.py) 
[`test_08_assert_files.py`](tests/14_plugins/01_assert/test_08_assert_files.py) 
[`test_09_assert_objects.py`](tests/14_plugins/01_assert/test_09_assert_objects.py) 
[`test_10_assert_filtering.py`](tests/14_plugins/01_assert/test_10_assert_filtering.py) 
[`test_10_assert_sorting.py`](tests/14_plugins/01_assert/test_11_assert_sorting.py)  
**Plugin docs**: 
[`plugin page`](https://pypi.org/project/assertpy/) 
[`full documentation on github`](https://github.com/assertpy/assertpy)  
___
[`pytest-rerunfailures`](#contents)
-
Re-run tests plugin to eliminate flaky failures. Provides CLI options to re-run all failed tests and decorator to re-run single flaky test.
### Mark to re-run single flaky test
```python
# re-run individual failures. All parameters are optional. 
# default re-run count is 1. Delay time in seconds.
@pytest.mark.flaky(reruns=5, reruns_delay=2, condition=sys.platform.startswith("win32"))
def test_rerun():
    assert random.choice([True, False])

# re-runs any except ValueError
@pytest.mark.flaky(rerun_except="ValueError")  
def test_rerun_except():
    raise ValueError()

# re-runs only OSError or ValueError
@pytest.mark.flaky(reruns=3, only_rerun=["OSError", "ValueError"])
def test_rerun_only():
    raise OSError()
```
### CLI options to re-run all failed tests
```
# Re-run all failures
pytest --reruns 5

# Re-run all failures with 4 sec between re-runs
pytest --reruns 5 --reruns-delay 4

# Re-run all failures other than matching certain expressions
pytest --reruns=2 --rerun-except=ValueError --rerun-except=OSError

# Re-run all failures matching certain expressions
pytest --reruns=3 --only-rerun=ValueError
```
Note: This plugin may not be used with class, module, and package level fixtures.
**Code examples**: 
[`test_rerun_with_cli_flags.py`](tests/14_plugins/02_rerun/test_rerun_with_cli_flags.py) 
[`test_rerun_with_marks.py`](tests/14_plugins/02_rerun/test_rerun_with_marks.py)  
**Plugin docs**: 
[`plugin page with documentation`](https://pypi.org/project/pytest-rerunfailures)  
___
[`pytest-xdist`](#contents)
-
The pytest-xdist plugin extends pytest with new test execution modes, the most used being distributing tests across multiple CPUs to speed up test execution.
### Running tests across multiple CPUs
To send tests to multiple CPUs, use the -n (or --numprocesses) option:
```
# running in 3 processes:
pytest -n 3

# running as many processes as computer has CPU cores:
pytest -n auto
```
### The test distribution algorithm is configured with the `--dist` CLI option
* `--dist` (default): Sends pending tests to any worker that is available, without any guaranteed order. 
* `--dist` loadscope: Tests are grouped by module for test functions and by class for test methods. Groups are distributed to available workers as whole units. This guarantees that all tests in a group run in the same process. This can be useful if you have expensive module-level or class-level fixtures. Grouping by class takes priority over grouping by module.
* `--dist` loadfile: Tests are grouped by their containing file. Groups are distributed to available workers as whole units. This guarantees that all tests in a file run in the same worker.
* `--dist` loadgroup: Tests are grouped by the xdist_group mark. Groups are distributed to available workers as whole units. This guarantees that all tests with same xdist_group name run in the same worker. Example: `@pytest.mark.xdist_group(name="group1")`
```
# no group, any test to any worker, --dist=load is default
pytest -n=2 --dist=load

# group by class and module
pytest -n=2 --dist=loadscope

# group by file
pytest -n=2 --dist=loadfile

# group by mark, i.e. @pytest.mark.xdist_group(name="group1")
pytest -n=2 --dist=loadgroup
```
### Creating one log file for each worker
Due to how pytest-xdist is implemented, the `-s`/`--capture=no` option does not work.
```python
# content of conftest.py
def pytest_configure(config):  # hook for plugin configuration
    worker_id = os.environ.get("PYTEST_XDIST_WORKER")
    if worker_id is not None:
        logging.basicConfig(
            format=config.getini("log_file_format"),
            filename=f"tests_{worker_id}.log",
            level=config.getini("log_file_level"),
        )
```
When running the tests with `-n=3`, for example, three files will be created in the current directory: `tests_gw0.log`, `tests_gw1.log` and `tests_gw2.log`.
### Making session-scoped fixtures execute only once
pytest-xdist is designed so that each worker process will perform its own collection and execute a subset of all tests. This means that tests in different processes requesting a high-level scoped fixture (for example session) will execute the fixture code more than once, which breaks expectations and might be undesired in certain situations.

While pytest-xdist does not have a builtin support for ensuring a session-scoped fixture is executed exactly once, this can be achieved by using a lock file for inter-process communication.

The example below needs to execute the fixture session_data only once (because it is resource intensive, or needs to execute only once to define configuration options, etc), so it makes use of a FileLock to produce the fixture data only once when the first process requests the fixture, while the other processes will then read the data from a file.

```python
# conftest.py
import json

import pytest
from filelock import FileLock


@pytest.fixture(scope="session")
def session_data(tmp_path_factory, worker_id):
    if worker_id == "master":
        # not executing in with multiple workers, just produce the data and let
        # pytest's fixture caching do its job
        return produce_expensive_data()

    # get the temp directory shared by all workers
    root_tmp_dir = tmp_path_factory.getbasetemp().parent

    fn = root_tmp_dir / "data.json"
    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            data = json.loads(fn.read_text())
        else:
            data = produce_expensive_data()
            fn.write_text(json.dumps(data))
    return data
```
**Code examples**: 
[`test_01_parallel_load_default.py`](tests/14_plugins/03_parallel/test_01_parallel_load_default.py) 
[`test_02_parallel_load_scope.py`](tests/14_plugins/03_parallel/test_02_parallel_load_scope.py) 
[`test_03_parallel_load_file.py`](tests/14_plugins/03_parallel/test_03_parallel_load_file.py) 
[`test_04_parallel_load_group.py`](tests/14_plugins/03_parallel/test_04_parallel_load_group.py) 
[`test_05_parallel_log_workers.py`](tests/14_plugins/03_parallel/05_log_workers/test_05_parallel_log_workers.py) 
[`test_06_parallel_fixture.py`](tests/14_plugins/03_parallel/06_single_session_scope_fixture/test_06_parallel_fixture.py)    
**Plugin docs**: 
[`plugin page`](https://pypi.org/project/pytest-xdist/) 
[`full documentation page`](https://pytest-xdist.readthedocs.io)  
