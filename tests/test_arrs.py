import pytest
from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    with pytest.raises(IndexError):
        assert arrs.get([], 0, "test")


def test_get_default():
    assert arrs.get([1, 2, 3], -1, "test") == "test"



def test_my_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]


def test_my_slice_zero_list():
    assert arrs.my_slice([], 1, "test") == []


def test_my_slice_otr_1():
    assert arrs.my_slice([1, 2, 3, 4], -2) == [3, 4]

def test_my_slice_otr_2():
    assert arrs.my_slice([1, 2, 3, 4], -10) == [1, 2, 3, 4]