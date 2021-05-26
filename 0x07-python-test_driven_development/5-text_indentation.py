#!/usr/bin/python3
"""script print text"""

def text_indentation(text):
    """function print text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in text:

        if i == '.' or i == '?' or i == ':':
            print("{}\n".format(i))
        else:
            print(i, end='')
