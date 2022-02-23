"""Exercise 3 - Utils: List Utility functions."""

__author__ = "730484603"


def only_evens(user_list: list[int]) -> list[int]:
    """Returns a list containing only even elements of a given list."""
    i: int = 0
    evens: list[int] = list()
    while i < len(user_list):
        character: int = user_list[i]
        if character % 2 == 0:
            evens.append(character)
        i += 1
    return evens


def sub(given_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns a subset of the given list, between the stat index and the end index."""
    subset_list: list[int] = list()
    if start_index < 0:
        start_index = 0
    if end_index > len(given_list):
        end_index = len(given_list)
    if len(given_list) == 0 or start_index > len(given_list) or end_index <= 0:
        return subset_list
    while start_index < len(given_list) and start_index <= end_index - 1:
        character: int = given_list[start_index]
        subset_list.append(character)
        start_index += 1
    return subset_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Returns a list containing the first list, followed by the second list."""
    concatenated_list: list[int] = list()
    i: int = 0
    while i < len(list_one):    
        list_one_character: int = list_one[i]
        concatenated_list.append(list_one_character)
        i += 1
    i = 0
    while i < len(list_two):
        list_two_character: int = list_two[i]
        concatenated_list.append(list_two_character)
        i += 1
    return concatenated_list