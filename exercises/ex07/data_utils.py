"""Dictionary related utility functions."""

__author__ = "730484603"

# Define your functions below


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv inta a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the fule when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    
    if N >= len(table):
        N = len(table)

    for column in table:
        n_list: list[str] = []
        i: int = 0
        while N > i:
            item: str = table[column][i]
            n_list.append(item)
            i += 1
        result[column] = n_list

    return result


def select(column_table: dict[str, list[str]], new_columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    
    for column in new_columns:
        result[column] = column_table[column]
    
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    
    for column in table_one:
        result[column] = table_one[column]

    for column in table_two:
        if column in result:
            result[column] += table_two[column]
        else:
            result[column] = table_two[column]

    return result


def count(values: list[str]) -> dict[str, int]:
    """Count the number of times a value appears in the inputted list."""
    result: dict[str, int] = {}

    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result