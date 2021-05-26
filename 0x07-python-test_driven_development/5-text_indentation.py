#!/usr/bin/python3


def text_indentation(text):
    """function"""

    for i in text:
        if i == '.' or i == '?' or i == ':':
            print("{}\n".format(i))
        else:
            print(i, end='')
