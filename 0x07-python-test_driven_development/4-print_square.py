#!/usr/bin/python3


def print_square(size):
    """Functioon print # """
    if size == 0:
        print("")
    for row in range(size):
        for column in range(size):
            print("#", end='')
        print("")