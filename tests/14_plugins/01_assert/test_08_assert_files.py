import os
import shutil

import pytest
from assertpy import assert_that, contents_of


@pytest.fixture(autouse=True)
def foo_txt_file_for_test():
    with open('foo.txt', 'w') as file:
        file.write('foobar')
    yield
    os.remove('foo.txt')


@pytest.fixture(autouse=True)
def directory_for_test():
    os.makedirs('test_dir', exist_ok=True)
    yield
    shutil.rmtree('test_dir')


def test_assert_files():
    assert_that('foo.txt').exists()
    assert_that('missing.txt').does_not_exist()
    assert_that('foo.txt').is_file()

    assert_that('test_dir').exists()
    assert_that('missing_dir').does_not_exist()
    assert_that('test_dir').is_directory()

    contents = contents_of('foo.txt', 'ascii')
    assert_that(contents).starts_with('foo').ends_with('bar').contains('oob')