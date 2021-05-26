#!/usr/bin/python3
"""script of python 
print #"""

def print_square(size):
    """Functioon print # """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")
    for row in range(size):
        for column in range(size):
            print("#", end='')
        print("")
