"""My first program for one shot wordle."""
__author__ = "730651254"

hidden: str = "python"
idx: int = 0
win_idx: int = 0
word = input(f"What is your { len(hidden)}-letter guess? ")

while len(word) != len(hidden):
    word = input(f"That was not { len(hidden)} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
result: str = ""

while idx < len(hidden): 
    if word[idx] == hidden[idx]:
        result += GREEN_BOX 
        win_idx += 1
    elif word[idx] != hidden[idx]:
        testing: bool = False
        idx_y: int = 0
        while testing is False and idx_y < len(hidden):
            if word[idx] == hidden[idx_y]:
                testing = True
            else:
                idx_y += 1
        if testing is True:
            result += YELLOW_BOX
        if testing is False:
            result += WHITE_BOX
    idx += 1
if win_idx == 6:
    print(result)
    print("Woo! You got it!")
else:
    print(result)
    print("Not quite. Play again soon!")