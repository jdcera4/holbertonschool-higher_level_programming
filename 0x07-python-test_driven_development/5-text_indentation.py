#!/usr/bin/python3
"""script print text"""


def text_indentation(text):
    """function print text"""
    flag = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in text:
        if flag == 1 and i is ' ':
            print('', end='')
            flag = 0
            continue
        if i is '.' or i is '?' or i is ':':
            print("{}\n".format(i))
            flag = 1
        else:
            print(i, end='')
            flag = 0
