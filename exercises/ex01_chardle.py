"""Ex01 - Chardle - A cute step toward Worlde."""

__author__ = "730484603"

five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_character: str = input("Enter a single character: ")
if len(single_character) != 1: 
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + single_character + " in " + five_character_word)
if single_character == five_character_word[0]:
    print(single_character + " found at index 0")
if single_character == five_character_word[1]:
    print(single_character + " found at index 1")
if single_character == five_character_word[2]:
    print(single_character + " found at index 2")
if single_character == five_character_word[3]:
    print(single_character + " found at index 3")
if single_character == five_character_word[4]:
    print(single_character + " found at index 4")
counting_matching_character: int = 0
if single_character == five_character_word[0]:
    counting_matching_character = counting_matching_character + 1
if single_character == five_character_word[1]:
    counting_matching_character = counting_matching_character + 1
if single_character == five_character_word[2]:
    counting_matching_character = counting_matching_character + 1
if single_character == five_character_word[3]:
    counting_matching_character = counting_matching_character + 1
if single_character == five_character_word[4]:
    counting_matching_character = counting_matching_character + 1
if counting_matching_character == 0:
    print("No instances of " + single_character + " found in " + five_character_word)
else:
    if counting_matching_character == 1:
        print(str(counting_matching_character) + " instance of " + single_character + " found in " + five_character_word)
    else:
        if counting_matching_character > 1:
            print(str(counting_matching_character) + " instances of " + single_character + " found in " + five_character_word)