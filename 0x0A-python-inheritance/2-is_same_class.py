#!/usr/bin/python3
"""function that returns True if the object is exactly an instance 
of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """Return false or True"""
    return True if type(obj) is a_class else False
