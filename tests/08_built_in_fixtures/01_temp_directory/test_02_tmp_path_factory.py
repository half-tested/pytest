import pytest

CONTENT = "content"


@pytest.fixture(scope="session")
def data_dir(tmp_path_factory):
    return tmp_path_factory.mktemp("data")


def test_tmp_path_factory_fixture_one(data_dir):
    temp_file = data_dir / "example.txt"
    temp_file.write_text(CONTENT)
    print("\n", data_dir)
    assert temp_file.read_text() == CONTENT
    assert len(list(data_dir.iterdir())) == 1


def test_tmp_path_factory_fixture_two(data_dir):
    temp_file = data_dir / "example.txt"
    print("\n", data_dir)
    assert temp_file.read_text() == CONTENT
    assert len(list(data_dir.iterdir())) == 1
