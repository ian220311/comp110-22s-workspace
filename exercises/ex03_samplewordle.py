"""Exercise 3 - Structured Wordle."""

__author__ = "730484603"


def contains_char(string: str, character: str) -> bool:
    """Evaluates whether a single character is located within a string."""
    assert len(character) == 1
    i: int = 0
    tracking_character: bool = False
    while tracking_character is not True and i < len(string):
        if string[i] == character:
            tracking_character = True
        else:
            i += 1
    if tracking_character is True:
        return True
    else:
        return False

def emojified(player_guess: str, secret_word: str) -> str:
    """Returns emoji string whose color codifies"""
    assert len(player_guess) == len(secret_word)
    i: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    resulting_emoji: str = ""
    while i < len(player_guess):
        if player_guess[i] == secret_word[i]:
            resulting_emoji += GREEN_BOX
        else:
            if contains_char(secret_word, player_guess[i]) is True:
                resulting_emoji += YELLOW_BOX
            else:
                resulting_emoji += WHITE_BOX
        i += 1
    return resulting_emoji 

def input_guess(expected_length: int) -> str:
    """Give an expected lenght of a guess."""
    guess_length: str = str(input(f"Enter a {expected_length} character word: "))
    while expected_length != len(guess_length):
        guess_length = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess_length

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    N: int = 1
    won: bool = False
    while N <= 6 and won is not True:  
        print(f"=== Turn {N}/6 ===")
        guess: str = input(input_guess(len(secret)))
        print(emojified(guess, secret))
        N += 1   
        if guess == secret:
            won = True
            print(f"You won in {N - 1}/6 turns!")
    if N > 6 and won is not True:
        print("X/6 - Sorry, try again tommorow!")