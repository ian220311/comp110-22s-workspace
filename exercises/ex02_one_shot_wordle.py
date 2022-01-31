"""Exercise Two for COMP110: One Shot Wordle"""

__author__ = "730484603"

secret_word: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
resulting_emoji: str = ""
guessed_character_identified: bool = False
alternative_indices: int = 0
user_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
while len(secret_word) != len(user_guess):
    user_guess = input(f"That was not {len(secret_word)} letters! Try again: ")
while i < len(secret_word):
    if secret_word[i] == user_guess[i]:
        resulting_emoji += GREEN_BOX
    else:
        while guessed_character_identified == (not True) and i < len(secret_word):
            if secret_word[alternative_indices] == user_guess[i]:
                guessed_character_identified = True
            else:
                alternative_indices += 1
        if guessed_character_identified == True:
            resulting_emoji += YELLOW_BOX
        else:
            resulting_emoji += WHITE_BOX
    i += 1
print(resulting_emoji)
if secret_word == user_guess:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
