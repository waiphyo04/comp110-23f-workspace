"""Example functions to learn definition and calling syntax"""

def my_max(number1: int, number2: int) -> int: #this top line is the signature of the function #num1 and num2 are parameters
    if number1 >= number2:
        return(number1)
    else:
        return(number2)
max_number: int = my_max(1,10)
another_max_number: int = my_max(2,6)

print(max_number)
print(another_max_number)
    