"""Test my zip function."""
__author__ = "73651254"


from lessons.zip import zip

def test_empty_list():
    """Testing empty list."""
    assert zip([], []) == {}


def test_list_length():
    """Testing list length."""
    test_list_1: list[str] = ["apple"]
    test_list_2: list[int] = [2]
    assert zip(test_list_1, test_list_2) == {"apple": 2}


def test_list_length_2():
    """Testing list length for 2nd time."""
    test_list_1: list[str] = ["apple", "banana", "orange"]
    test_list_2: list[int] = [2, 4, 1]
    assert zip(test_list_1, test_list_2) == {"apple": 2, "banana": 4, "orange": 1}