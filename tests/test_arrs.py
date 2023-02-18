import pytest
from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    with pytest.raises(IndexError):
        assert arrs.get([], 0, "test")


def test_get_default():
    assert arrs.get([1, 2, 3], -1, "test") == "test"


@pytest.fixture
def datas():
    return [1, 2, 3, 4]

def test_my_slice(datas):
    assert arrs.my_slice(datas, 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]


def test_my_slice_zero_list():
    assert arrs.my_slice([], 1, "test") == []


def test_my_slice_otr_1(datas):
    assert arrs.my_slice(datas, -2) == [3, 4]

def test_my_slice_otr_2(datas):
    assert arrs.my_slice(datas, -10) == [1, 2, 3, 4]