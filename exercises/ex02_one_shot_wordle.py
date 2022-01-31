"""Exercise Two: One Shot Wordle."""

__author__ = "730484603"

secret_word: str = "python"
player_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
resulting_emoji: str = ""

while len(secret_word) != len(player_guess):
    player_guess = input(f"That was not {len(secret_word)} letters! Try again: ")

if len(secret_word) == len(player_guess):
    while i < len(player_guess):
        if secret_word[i] == player_guess[i]:
            resulting_emoji += GREEN_BOX
        else:
            tracking_character: bool = False
            alternative_index: int = 0
            while tracking_character is not True and alternative_index < len(secret_word):
                if secret_word[alternative_index] == player_guess[i]:
                    tracking_character = True
                else:
                    alternative_index += 1
            if tracking_character is True:
                resulting_emoji += YELLOW_BOX
            else:
                resulting_emoji += WHITE_BOX
        i += 1
    print(resulting_emoji)
    if secret_word == player_guess:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!") 
