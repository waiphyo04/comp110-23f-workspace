"""My third program for wordle game."""
__author__ = "730651254"


def contains_char(secret_2: str, guess_char: str) -> bool:
    """Contains_char."""
    assert len(guess_char) == 1
    i_y: int = 0
    testing: bool = False
    while i_y < len(secret_2):
        if secret_2[i_y] == guess_char:
            testing = True
            i_y = len(secret_2)
        else:
            testing = False
        i_y += 1
    return testing


def emojified(guess_1: str, secret_1: str) -> str:
    """Emojified."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(secret_1) == len(guess_1)
    i: int = 0
    result: str = ""
    while i < len(secret_1):
        if guess_1[i] == secret_1[i]:
            result += GREEN_BOX
        else:
            if contains_char(secret_1, guess_1[i]):
                result += YELLOW_BOX
            else:
                result += WHITE_BOX
        i += 1
    return result


def input_guess(num_char: int) -> str:
    """Input_guess."""
    guess = input(f"Enter a {num_char} character word: ")
    while num_char != len(guess):
        guess = input(f"That wasn't {num_char} chars! Try again: ")
    return guess                   


def main() -> None:
    """main_function."""
    secret = "wordle"
    t_idx: int = 1
    while t_idx < 7:
        print(f"=== Turn {t_idx}/6 ===")
        your_guess = input_guess(len(secret))
        if your_guess == secret:
            print(emojified(your_guess, secret))
            print(f"You won in {t_idx}/6 turns!")
            t_idx = 7   
        else:
            print(emojified(your_guess, secret))
        t_idx += 1
    if t_idx == 7:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()