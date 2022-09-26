#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    find the values divisible by two in list
    Args:
        my_list - list to search
    Return:
        list of True or False
    """
    return list(map(lambda x: False if x % 2 else True, my_list))


if __name__ == '__main__':
    tmp = list(range(25))
    tmp2 = divisible_by_2(tmp)
    for a, b in zip(tmp, tmp2):
        print(a, ':', b)
