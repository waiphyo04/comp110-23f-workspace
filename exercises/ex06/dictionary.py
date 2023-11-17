"""Dictionary exercise."""
__author__ = "730651254"


def invert(org_dict: dict[str, str]) -> dict[str, str]:
    """Challenge_1."""
    inverted_dict: dict[str, str] = {}
    for x in org_dict:
        y = org_dict[x]
        if y in inverted_dict:
            raise KeyError
        inverted_dict[y] = x
    return inverted_dict


def favorite_color(color_dict: dict[str, str] = {}) -> str:
    """Challenge_2."""
    new_dict: dict[str, int] = {}
    for x in color_dict:
        y = color_dict[x]
        if y in new_dict: 
            new_dict[y] += 1
        else:
            new_dict[y] = 1
    largest: int = 0
    fav_color: str = ""
    for x in new_dict:
        if new_dict[x] > largest:
            largest = new_dict[x]
            fav_color = x
    return fav_color


def count(check_list: list[str]) -> dict[str, int]:
    """Challenge_3."""
    dictionary: dict[str, int] = {}
    for x in check_list:
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1
    return dictionary


def alphabetizer(c_list: list[str]) -> dict[str, list[str]]: 
    """Challenge_4."""
    new_dict: dict[str, list[str]] = {}
    for word in c_list:
        if word[0].lower() in new_dict:
            new_dict[word[0].lower()].append(word)
        else:
            new_dict[word[0].lower()] = [word]
    return new_dict


def update_attendance(given_dict: dict[str, list[str]], day: str, name: str) -> dict[str, list[str]]:
    """Challenge_5."""
    if day in given_dict:
        if name not in given_dict[day]:
            given_dict[day].append(name)
        
    else:
        new_list: list[str] = []
        new_list.append(name)
        given_dict[day] = new_list
    return given_dict


input_list: list[str] = ["cat", "Apple", "boy", "angry", "car", "alpine", "baby", "bull"]
print(alphabetizer(input_list))