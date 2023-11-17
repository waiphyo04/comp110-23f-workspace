"""Dictionary Test Exercise."""
___author__ = "730651254"

from exercises.ex06.dictionary import invert, update_attendance, favorite_color, count, alphabetizer


def test_empty_invert():
    """Testing."""
    assert invert({}) == {}


def test_invert_1():
    """Testing."""
    input_dict: dict[str] = {'a': 'b', 'c': 'd', 'e': 'f'}
    assert invert(input_dict) == {'b': 'a', 'd': 'c', 'f': 'e'}


def test_invert_2():
    """Testing."""
    input_dict: dict[str] = {"apple": "red", "sky": "blue"}
    assert invert(input_dict) == {"red": "apple", "blue": "sky"}


def test_empty_favorite_color():
    """Testing."""
    assert favorite_color({}) == ""


def test_favorite_color_1():
    """Testing."""
    input_dict: dict[str] = {"John": "Yellow", "Paul": "Blue", "Chris": "Blue"}
    assert favorite_color(input_dict) == "Blue"


def test_favorite_color_2():
    """Testing."""
    input_dict: dict[str] = {"John": "Yellow", "Paul": "Blue", "Chris": "Red", "Jena": "Red"}
    assert favorite_color(input_dict) == "Red"


def test_empty_count():
    """Testing."""
    assert count([]) == {}


def test_count_1():
    """Testing."""
    input_list: list[str] = ['a', 'b', 'c', 'a', 'c', 'b', 'd']
    assert count(input_list) == {'a': 2, 'b': 2, 'c': 2, 'd': 1}


def test_count_2():
    """Testing."""
    input_list: list[str] = ['a', 'b']
    assert count(input_list) == {'a': 1, 'b': 1}


def test_empty_alphabetizer():
    """Testing."""
    assert alphabetizer([]) == {}


def test_alphabetizer_1():
    """Testing."""
    input_list: list[str] = ["cat", "apple"]
    assert alphabetizer(input_list) == {'a': ["apple"], 'c': ["cat"]}


def test_alphabetizer_2():
    """Testing."""
    input_list: list[str] = ["apple"]
    assert alphabetizer(input_list) == {'a': ["apple"]}


def test_empty_update_attendance():
    """Testing."""
    assert update_attendance({}, "Tuesday", "Harry") == {"Tuesday": ["Harry"]}


def test_update_attendance_1():
    """Testing."""
    input_dict: dict[str, list[str]] = {"Monday": ["John", "Paul"], "Tuesday": ["Chris"]}
    expected_result = {"Monday": ["John", "Paul"], "Tuesday": ["Chris", "Harry"]}
    assert update_attendance(input_dict, "Tuesday", "Harry") == expected_result


def test_update_attendance_2():
    """Testing."""
    input_dict: dict[str, list[str]] = {"Monday": ["John", "Paul"], "Tuesday": ["Chris"]}
    expected_result = {"Monday": ["John", "Paul"], "Tuesday": ["Chris"], "Wednesday": ["Alyssa"]}
    assert update_attendance(input_dict, "Wednesday", "Alyssa") == expected_result