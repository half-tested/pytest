import pytest

CONTENT = "hello world"


# tmp_path_factory is a session scope fixture
@pytest.fixture(scope="session")
def data_file(tmp_path_factory):
    temp_dir = tmp_path_factory.mktemp("data")
    temp_file = temp_dir / "example.txt"
    temp_file.write_text(CONTENT)
    print("\n", temp_file)
    return temp_file


def test_tmp_path_factory_fixture_one(data_file):
    assert 'hello' in data_file.read_text()


def test_tmp_path_factory_fixture_two(data_file):
    assert 'world' in data_file.read_text()
