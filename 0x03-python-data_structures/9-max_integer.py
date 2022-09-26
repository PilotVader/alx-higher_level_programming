#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    find the maximum value of a list
    Args:
        my_list - list to search
    Return:
        None - if list is empty
        maximum of list
    """
    L = len(my_list)
    if L == 0:
        return None
    Max = my_list[0]
    for elem in my_list:
        if elem > Max:
            Max = elem
    return 
