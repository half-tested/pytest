CONTENT = "content"


def test_tmp_path_fixture(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT)
    print("\n", tmp_path)
    assert p.read_text() == CONTENT
    assert len(list(tmp_path.iterdir())) == 1


"""
pytest.ini temp folders usage setup:

1. https://docs.pytest.org/en/stable/reference/reference.html#confval-tmp_path_retention_count
set how many sessions should we keep the tmp_path directories (default 3)
    [pytest]
    tmp_path_retention_count = 3
    
2. https://docs.pytest.org/en/stable/reference/reference.html#confval-tmp_path_retention_policy
control which directories created by the tmp_path fixture are kept around, based on test outcome (default all)
  * all: retains directories for all tests, regardless of the outcome
  * failed: retains directories only for tests with outcome error or failed
  * none: directories are always removed after each test ends, regardless of the outcome
    [pytest]
    tmp_path_retention_policy = "all"
"""
