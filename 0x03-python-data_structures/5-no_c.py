#!/usr/bin/python3

def no_c(my_str):
    """
    Returns a copy of my_str without c or C
    Args:
        my_str - the string to filter
    """
    return "".join(filter(lambda x: x not in 'cC', my_str))
