#!/usr/bin/python3
"""Check for proper number of args"""
from os import path
from sys import argv, stderr

if __name__ == "__main__":
    if len(argv) < 2:
        stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    for f in argv:
        f = './' + f
        if not path.isfile(f):
            stderr.write("Missing {}\n".format(f))
            exit(1)

    exit(0)
