import json

import pytest
from filelock import FileLock


def produce_expensive_data():
    return 'produced data'


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
