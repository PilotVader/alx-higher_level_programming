#!/usr/bin/python3

def add_tuple(a=(), b=()):
    """
    add the fisrst and second elems of a b
    if any of a or b has less than 2 elems
    0 is padded
    Args:
        a - tuple default empty
        b - tuple default empty
    Return:
        (c, d)
    """
    while len(a) < 2:
        a = (*a, 0)
    while len(b) < 2:
        b = (*b, 0)
    return a[0] + b[0], a[1] + b[1]


if __name__ == '__main__':
    a = (1, 89)
    b = (88, 11)
    print(add_tuple(a, b))
    print(add_tuple(a, (1,)))
    print(add_tuple(a, ()))
