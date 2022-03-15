"""Exercise 6: Edge and Used cases for Dictionary Functions."""

__author__ = "730484603"

from exercises.ex06.dictionary import invert, favorite_color, count

import pytest


def test_invert_key_error() -> None:
    """Key Error test for invert function."""
    with pytest.raises(KeyError):
        given_dictionary = {'ian': 'jaras', 'gi': 'jaras'}
        invert(given_dictionary)


def test_invert_empty() -> None:
    """Test the return of the invert function with an empty dictionary."""
    xs: dict[str, str] = {} 
    assert invert(xs) == {}


def test_invert_regular_parameters_names() -> None:
    """First test for the return of the invert function with first and last names as regular parameters."""
    xs: dict[str, str] = {'ian': 'jaras', 'gi': 'chen'}
    assert invert(xs) == {'jaras': 'ian', 'chen': 'gi'}


def test_invert_regular_parameters_schools() -> None:
    """Second test for the return of the invert function with name and school as regular parameters."""
    xs: dict[str, str] = {'ian': 'UNC', 'quinn': 'USNA', 'ricky': 'NCSU'}
    assert invert(xs) == {'UNC': 'ian', 'USNA': 'quinn', 'NCSU': 'ricky'}


def test_favorite_color_empty() -> None:
    """Test the return of the favorite color function with an empty dictionary."""
    xs: dict[str, str] = {} 
    assert favorite_color(xs) == ""


def test_favorite_color_regular_parameters_one() -> None:
    """First test for the return of the favorite color function with regular parameters."""
    xs: dict[str, str] = {'ian': 'carolina blue', 'gi': 'carolina blue'}
    assert favorite_color(xs) == 'carolina blue'


def test_favorite_color_regular_parameters_tie() -> None:
    """Second test for the return of the favorite color function with a tie for most popular color."""
    xs: dict[str, str] = {'ricky': 'red', 'quinn': 'navy', 'ian': 'carolina blue', 'cory': 'red', 'om': 'teal', 'cam': 'teal'}
    assert favorite_color(xs) == 'red'


def test_count_empty_list() -> None:
    """Test the return of the count function with an empty list."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_regular_parameters_one() -> None:
    """First test for the return of the count function with names as regular parameters."""
    xs: list[str] = ['ian', 'ian', 'ian', 'gi', 'gi', 'gi']
    assert count(xs) == {'ian': 3, 'gi': 3}


def test_count_regular_parameters_two() -> None:
    """Second test for the return of the count function with colors as regular parameters."""
    xs: list[str] = ['blue', 'blue', 'blue', 'red', 'green', 'blue', 'teal', 'yellow', 'yellow', 'carolina blue', 'black', 'black', 'brown', 'brown']
    assert count(xs) == {'blue': 4, 'red': 1, 'green': 1, 'teal': 1, 'yellow': 2, 'carolina blue': 1, 'black': 2, 'brown': 2}