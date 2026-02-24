import pytest
import random
from tasks.find_repeat_2 import find_repeat

@pytest.mark.parametrize("arr, expected", [
    ([1, 2, 4, 5, 6, 1, 0, 3], 1),
    ([0, 0, 0, 0], 0),
    ([0, 0], 0),
    ([0, 1, 2, 3, 4, 5, 0], 0),
    ([5, 4, 3, 2, 1, 1, 0], 1),
    ([0, 1, 2, 3, 4, 5, 5], 5),
])
def test_simple_cases(arr, expected):
    result = find_repeat(len(arr), arr)
    assert result == expected


def test_multiple_duplicates():
    arr = [1, 2, 3, 2, 1, 4]
    result = find_repeat(len(arr), arr)
    assert result in (1, 2)


def test_no_modification():
    arr = [1, 2, 3, 1, 4]
    original = arr.copy()
    find_repeat(len(arr), arr)
    assert arr == original


def test_large_n():
    n = 1000000
    arr = list(range(n-1)) + [0]
    random.shuffle(arr)
    result = find_repeat(len(arr), arr)
    assert result == 0


def test_large_many_duplicates():
    arr = list(range(10000)) + [5, 17]
    random.shuffle(arr)
    result = find_repeat(len(arr), arr)
    assert result in (5, 17)