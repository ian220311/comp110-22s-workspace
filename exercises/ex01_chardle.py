"""Ex01 - Chardle - A cute step toward Worlde."""

__author__ = "730484603"

word1: str = input("Enter a 5-character word: ")
if len(word1) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character1: str = input("Enter a single character: ")
if len(character1) != 1: 
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character1 +  " in " + word1)
if character1 == word1[0]:
    print(character1 + " found at index 0")
if character1 == word1[1]:
    print(character1 + " found at index 1")
if character1 == word1[2]:
    print(character1 + " found at index 2")
if character1 == word1[3]:
    print(character1 + " found at index 3")
if character1 == word1[4]:
    print(character1 + " found at index 4")
matching: int = 0
if character1 == word1[0]:
    matching = matching + 1
if character1 == word1[1]:
    matching = matching + 1
if character1 == word1[2]:
    matching = matching + 1
if character1 == word1[3]:
    matching = matching + 1
if character1 == word1[4]:
    matching = matching + 1
if matching == 0 :
    print("No instances of " + character1 + " found in " + word1)
else:
    if matching == 1:
        print(str(matching) + " instance of " + character1 + " found in " + word1)
    else:
        if matching > 1:
            print(str(matching) + " instances of " + character1 + " found in " + word1)
