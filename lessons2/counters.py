"""Practicing Counters and commenting"""

# Initialize the string I want to count the odds of
num_string: str = "243"
# Initialize my counter for number of odds
num_of_odd: int = 0

if int(num_string[0]) % 2 == 1:
    # If the element at index is odd, increase the counter by 1
    num_of_odd = num_of_odd + 1
if int(num_string[1]) % 2 == 1:
    """If the element at index is odd, 
    increase the counter by 1"""
    num_of_odd = num_of_odd + 1
if int(num_string[2]) % 2 == 1:
    num_of_odd = num_of_odd + 1
print(num_of_odd)
