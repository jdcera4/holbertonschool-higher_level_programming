#!/usr/bin/python3
"""Script of python add integers"""


def add_integer(a, b=98):
    """Add function"""
    if not isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
