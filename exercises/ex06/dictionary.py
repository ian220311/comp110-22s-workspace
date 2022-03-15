"""Exercise 6: Dictionary Functions."""

__author__ = "730484603"


def invert(given_dictionary: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of [str, str] the keys and the values will be inverted."""
    inverted_dictionary: dict[str, str] = dict()
    for key in given_dictionary:
        if given_dictionary[key] in inverted_dictionary:
            raise KeyError
        inverted_dictionary[given_dictionary[key]] = key
    return inverted_dictionary


def favorite_color(favorite_colors: dict[str, str]) -> str:
    """Returns a str which is the color that appears most frequently."""
    frequency: dict[str, int] = dict()
    for key in favorite_colors:
        if favorite_colors[key] in frequency:
            frequency[favorite_colors[key]] += 1
        else:
            frequency[favorite_colors[key]] = 1
    max_frequency: int = 0
    fav_color: str = ""
    for color in frequency:
        if frequency[color] > max_frequency:
            max_frequency = frequency[color]
            fav_color = color
    return fav_color


def count(given_list: list[str]) -> dict[str, int]:
    """Produce a dictionary where each key is unique value in the given list, and the value is its frequency."""
    key_frequency: dict[str, int] = dict()
    for item in given_list: 
        if str(item) in key_frequency:
            key_frequency[str(item)] += 1
        else:
            key_frequency[str(item)] = 1
    return key_frequency
