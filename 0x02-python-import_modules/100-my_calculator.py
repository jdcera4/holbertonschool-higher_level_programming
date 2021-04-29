#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

def main():
    argc = len(argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argc > 1:
        if argv[2] == '+':
            c = add(int(argv[1]), int(argv[3]))
            print("{} + {} = {}".format(argv[1], argv[3], c))
        elif argv[2] == '-':
            c = sub(int(argv[1]), int(argv[3]))
            print("{} - {} = {}".format(argv[1], argv[3], c))
        elif argv[2] == '*':
            c = mul(int(argv[1]), int(argv[3]))
            print("{} * {} = {}".format(argv[1], argv[3], c))
        elif argv[2] == '/':
            c = div(int(argv[1]), int(argv[3]))
            print("{} / {} = {}".format(argv[1], argv[3], c))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

if __name__ == "__main__":
    main()
