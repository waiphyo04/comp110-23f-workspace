"""Dictionary related utility functions."""

__author__ = "730651254"
# Define your functions below

from csv import DictReader 

def read_csv_rows(filename: str) ->list[dict[str, str]]:
    """Read a csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()

    return result




def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns value in a table column under a specific header"""
    result: list[str] = []
    for row in table:
        #append every value under key header
        result.append(row[header])
    return result

def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with colummn hearders as keys"""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table 
    #first_row: dict[str, str] = table[0]
    for key in table[0]: #first_row:
        result[key] = column_vals(table, key)
    return result