#!/usr/bin/python3
"""Read file using open"""


def read_file(filename=""):
    """Print file (UTF8) it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
