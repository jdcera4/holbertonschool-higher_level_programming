#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max = 0
    a = ''
    for key, i in a_dictionary.items():
        if i > max:
            max = i
            a = key
    return a
