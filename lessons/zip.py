"""Combining two lists into a dictionary."""
__author__ = "730651254"


def zip(list_1: list[str], list_2: list[int]) -> dict[str, int]:
    """Dict creation."""
    if len(list_1) != len(list_2):
        return {}
    new_dictionary = {}
    for i in range(0, len(list_1)):
        new_dictionary[list_1[i]] = list_2[i] 
    return new_dictionary 