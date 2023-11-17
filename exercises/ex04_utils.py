"""My learning journey."""


def all(number_list: list[int], num: int) -> bool:
    """All function."""
    result: bool = True
    if len(number_list) == 0:
        result = False
    else:
        
        i: int = 0
        i_check: int = 0
        while i < len(number_list):
            if number_list[i] == num:
                i_check += 1
                i += 1
            else:
                i += 1

        if i_check == len(number_list):
            result = True
        else:
            result = False
    return result


def max(number_list: list[int]) -> int:
    """Max function."""
    if len(number_list) == 0:
        raise ValueError("max() arg is an empty list")
    else:
        i: int = 1
        largest: int = number_list[0]
        while i < len(number_list):
            if number_list[i] > largest:
                largest = number_list[i]
            i += 1
    return (largest)


def is_equal(first: list[int], second: list[int]) -> bool:
    """is_equal function."""
    result: bool = True
    if len(first) != len(second):
        result = False
    else:
        i: int = 0
        true_check: int = 0
        while i < len(first):
            if first[i] == second[i]:
                true_check += 1
            i += 1
        if true_check == len(first):
            result = True
        else:
            result = False
    return result