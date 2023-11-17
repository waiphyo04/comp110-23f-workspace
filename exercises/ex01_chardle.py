"""My first program for Comp110."""
__author__ = "730651254"

char = input("Enter a 5-character word: ")
word0 = input("Enter a single character: ")
word_count: int = 0

if len(char) != 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(word0) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + word0 + " in " + char)

if word0 == char[0]: 
    print(word0 + " found at index 0")
    word_count += 1
if word0 == char[1]:
    print(word0 + " found at index 1")
    word_count += 1
if word0 == char[2]: 
    print(word0 + " found at index 2")
    word_count += 1
if word0 == char[3]: 
    print(word0 + " found at index 3")
    word_count += 1
if word0 == char[4]: 
    print(word0 + " found at index 4")
    word_count += 1
if word_count == 1:
    print("1 instance of " + word0 + " found in " + char)
else:
    if word_count > 1:
        print(str(word_count) + " instances of " + word0 + " found in " + char) 
    else:
        if word_count == 0:
            print("No instances of " + word0 + " found in " + char)