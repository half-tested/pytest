import pytest


@pytest.fixture(
    params=[("3+5", 8), ("2+4", 6)],
    ids=["sum check: 3+5=8", "sum check: 2+4=6"]
)
def fixture_sum(request):
    return request.param


def test_fixture_param_simple(fixture_sum):
    assert eval(fixture_sum[0]) == fixture_sum[1]


@pytest.fixture(params=[
    ([1, 2, 3], 6),
    ([4, 5, 6], 15),
])
def number_list(request):
    return request.param


def test_param_fixture_sum_list(number_list):
    numbers, expected_sum = number_list
    assert sum(numbers) == expected_sum


@pytest.fixture(
    params=[
        {"numbers": [1, 2, 3], "expected_sum": 6},
        {"numbers": [4, 5, 6], "expected_sum": 15}
    ],
    ids=[
        "sum of 1, 2, 3",
        "sum of 4, 5, 6"]
)
def number_list_key_val(request):
    return request.param


def test_param_fixture_sum_key_val(number_list_key_val):
    numbers = number_list_key_val["numbers"]
    expected_sum = number_list_key_val["expected_sum"]
    assert sum(numbers) == expected_sum