secret: str = "python"
guess = input("Type your 6 character long guess: ")
while len(guess) != len(secret):
    guess = input("Character count error. Type again: ")
    
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
result: str = ""
testing: bool = False

for x in guess:
    for y in secret:
        if x == y:
            result += GREEN_BOX
        else:
            testing is False
            while testing is False:
                for z in secret:
                    if x == z:
                        testing == True
                    else:
                        testing is False
                if testing is True:
                    result += YELLOW_BOX
                if testing is False:
                    result += WHITE_BOX

print(result)
        