#!/usr/bin/python3
"""Print the list, but sorted"""


class MyList(list):
    """Class print the list, sorted"""

    def print_sorted(self):
        print(sorted(self))
