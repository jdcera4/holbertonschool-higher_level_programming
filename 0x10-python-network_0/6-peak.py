#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Args:
        list of integers
    """
    size = len(list_of_integers)
    size_c = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        size_c = size_c // 2
        if (mid < size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if size_c // 2 == 0:
                size_c = 2
            mid = mid + size_c // 2
        elif size_c > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if size_c // 2 == 0:
                size_c = 2
            mid = mid - size_c // 2
        else:
            return list_of_integers[mid]
