#String starts with a capital letter.
#String has an even number of quotation marks.
#String ends with one of the following sentence termination characters: ".", "?", "!"
#String has no period characters other than the last character.
#Numbers below 13 are spelled out (”one”, “two”, "three”, etc…).


def test_if_valid(input: str):
    result: bool = True
    if not input[0].isupper():
        result = False
        return result

    if input.count('"') % 2 != 0:
        result = False
        return result
    
    if input[len(input)- 1] not in ".?!":
        result = False
        return result
    
    if input.count(".") > 1 and input[len(input)- 1] != ".":
        result = False
        return result
    
    
    
    for x in range(0, len(input)):
        if input[x].isdigit():
            # Check if next character is also a digit (for two-digit numbers)
            if x + 1 < len(input) and input[x + 1].isdigit():
                check = str(input[x] + input[x + 1])
                num = int(check)
                # Ignore numbers greater than 12
                if num < 13: 
                    result = False
                    return result
            else:
                num = int(input[x])
                # Ignore numbers greater than 12
                if num < 13: 
                    result = False
                    return result
    """
    for x in range(0, len(input)):
        if input[x].isdigit():
            if x + 1 < len(input) and input[x + 1].isdigit():
                check = str(input[x] + input[x + 1])
                num = int(check)
                if num < 13: 
                    #num_list: list[str] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
                    #if num != num_list[num - 1]:
                    result = False
                    return result
            
            num = int(input[x])
            if num < 13: 
                #num_list: list[str] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
                #if num != num_list[num - 1]:
                result = False
                return result
        """
    
    return result
       
            
print(test_if_valid("You are 14 great."))

"""

def test_if_valid(input_str: str) -> bool:
    if not input_str[0].isupper():
        return False

    if input_str.count('"') % 2 != 0:
        return False

    if input_str[-1] not in ".?!":
        return False
    
    if input_str.count('.') > 1 and input_str[-1] == '.':
        return False

    num_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
    for word in num_words:
        if word in input_str:
            return False

    return True

# Example usage
print(test_if_valid("You are 2 great."))
"""
def is_valid_sentence(sentence):
    # Check if the sentence starts with a capital letter
    if not sentence[0].isupper():
        return False
    
    # Check for an even number of quotation marks
    if sentence.count('"') % 2 != 0:
        return False

    # Check if the sentence ends with a valid termination character
    if sentence[-1] not in ".?!":
        return False

    # Check for any periods other than the last character
    if '.' in sentence[:-1]:
        return False

    # Check for numbers below 13
    words = sentence.split()
    numbers_below_13 = {
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve'
    }
    for word in words:
        if word.isdigit() and int(word) < 13:
            return False
        if word in numbers_below_13:
            return False

    return True

# Example usage
sentence = "This is a valid. sentence."
print(is_valid_sentence(sentence))