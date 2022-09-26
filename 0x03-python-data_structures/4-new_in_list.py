#!/usr/bin/python3

def new_in_list(my_list, idx, elem):
    """
    replace an elment from a list at index idx with elem
    Args:
        my_list - list to search
        idx - the position to access
        elem - new elem to swap with
    Return:
        modified my_list
    """
    copy = my_list[:]
    if idx < 0 or idx >= len(copy):
        return copy
    copy[idx] = elem
    return copy

