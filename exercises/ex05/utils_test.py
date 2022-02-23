"""Exercise 5 - Unit Tests for list utility functions."""

__author__ = "730484603"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty_list() -> None:
    """Test the return of an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_single_odd_item() -> None:
    """Test the return of a single odd integer."""
    xs: list[int] = [1]
    assert only_evens(xs) == []


def test_only_evens_single_even_item() -> None:
    """Test the return of a single even integer."""
    xs: list[int] = [2]
    assert only_evens(xs) == [2]


def test_only_evens_odds_list() -> None:
    """Test the return of a list of odd integers."""
    xs: list[int] = [1, 3, 5, 7, 9, 11, 13]
    assert only_evens(xs) == []


def test_only_evens_evens_list() -> None:
    """Test the return of a list of even integers."""
    xs: list[int] = [2, 4, 6, 8, 10, 12]
    assert only_evens(xs) == [2, 4, 6, 8, 10, 12]


def test_only_evens_mixed_integers_list() -> None:
    """Test the return of a list of evena and odd integers."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    assert only_evens(xs) == [2, 4, 6, 8, 10, 12]


def test_sub_empty_list() -> None:
    """Test the return of of an empty list."""
    xs: list[int] = []
    assert sub(xs, 1, 4) == []


def test_sub_negative_start_index() -> None:
    """Test the return of a negative start index."""
    xs: list[int] = [1, 2, 3]
    negative_start_index: int = -3
    assert sub(xs, negative_start_index, 3) == [1, 2, 3]


def test_sub_end_index_greater_lenght() -> None:
    """Test the return of a end index greater than the lenght of the given index."""
    xs: list[int] = [1, 2, 3]
    greater_end_index: int = 13
    assert sub(xs, 0, greater_end_index) == [1, 2, 3]


def test_sub_iregular_parameters() -> None:
    """Test the return of sub function with iregular paramaters, including negative start index and end index greater than the length of given idex."""
    xs: list[int] = [1, 2, 3, 5, 6]
    negative_start_index: int = -13
    greater_end_index: int = 22
    assert sub(xs, -13, 22) == [1, 2, 3, 5, 6]


def test_sub_regular_paramaters() -> None:
    """Test the return of sub function with regular paramaters."""
    xs: list[int] = [1, 2, 3, 5, 6]
    assert sub(xs, 1, 3) == [2, 3]


def test_sub_regular_paramaters_two() -> None:
    """Second version of a test for the return of sub function with regular paramaters."""
    xs: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    assert sub(xs, 4, 9) == [50, 60, 70, 80, 90]


def test_sub_regular_paramaters_random_list() -> None:
    """Test the return of sub function with regular paramaters with random integers."""
    xs: list[int] = [13, 29, 1976, 22, 19, 2003, 6, 9, 21]
    assert sub(xs, 3, 6) == [22, 19, 2003]


def test_concat_empty_list_one() -> None:
    """Test the return when list one is empty."""
    example_list_one: list[int] = []
    example_list_two: list[int] = [7, 8, 9, 10, 11, 12]
    assert concat(example_list_one, example_list_two) == [7, 8, 9, 10, 11, 12]


def test_concat_empty_list_two() -> None:
    """Test the return when list two is empty."""
    example_list_one: list[int] = [1, 2, 3, 4, 5, 6]
    example_list_two: list[int] = []
    assert concat(example_list_one, example_list_two) == [1, 2, 3, 4, 5, 6]


def test_concat_empty_lists() -> None:
    """Test the return when list one and list two are empty."""
    example_list_one: list[int] = []
    example_list_two: list[int] = []
    assert concat(example_list_one, example_list_two) == []


def test_concat_regular_lists() -> None:
    """Test the return when list one and list two are regular lists."""
    example_list_one: list[int] = [1, 2, 3, 4, 5, 6]
    example_list_two: list[int] = [7, 8, 9, 10, 11, 12]
    assert concat(example_list_one, example_list_two) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def test_concat_random_lists() -> None:
    """Test the return when list one and list two are regular lists."""
    example_list_one: list[int] = [0, 6, 22, 2003, 18]
    example_list_two: list[int] = [0, 9, 13, 2002, 19]
    assert concat(example_list_one, example_list_two) == [0, 6, 22, 2003, 18, 0, 9, 13, 2002, 19]


def test_concat_list_order() -> None:
    """Test the return order of list one and list two. List two follows list one."""
    example_list_one: list[int] = [11, 27, 18, 23, 3]
    example_list_two: list[int] = [29, 5, 31, 26, 1066]
    assert concat(example_list_one, example_list_two) == [11, 27, 18, 23, 3, 29, 5, 31, 26, 1066]