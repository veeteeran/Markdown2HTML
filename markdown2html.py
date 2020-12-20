#!/usr/bin/python3
"""Check for proper number of args"""
from os import path
from sys import argv, stderr

if __name__ == "__main__":
    print(len(argv))
    if len(argv) < 3:
        stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    if not path.isfile(argv[1]):
        stderr.write("Missing {}\n".format(argv[1]))
        exit(1)
