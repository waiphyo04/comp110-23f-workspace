"""Summing the elements of a list using different loops."""


def w_sum(a_check_list: list[float]) -> float:
    """w_sum_function."""
    i: int = 0
    sum: float = 0.0
    while i < len(a_check_list):
        sum = sum + a_check_list[i]
        i += 1
    return sum


def f_sum(b_check_list: list[float]) -> float:
    """f_sum_function."""
    sum: float = 0.0
    for x in b_check_list:
        sum += x
    return sum


def f_range_sum(c_check_list: list[float]) -> float:
    """f_range_sum_function."""
    sum: float = 0.0
    for count in range(0, len(c_check_list), 1):
        numbers: float = c_check_list[count]
        sum += numbers
    return sum


"""count = int(input("Numbers would you like to include: "))
i: int = 0
vals: list[float] = []
while i < count:
    num = float(input("Enter a number: "))
    vals.append(num)
    i += 1

print(w_sum(vals,count))
print(f_sum(vals,count))
print(f_range_sum(vals,count))"""