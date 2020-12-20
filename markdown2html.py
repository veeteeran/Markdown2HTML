#!/usr/bin/python3
"""Check for proper number of args"""
from os import path
from sys import argv, stderr

def headings(read_file="", write_file=""):
    """
    Convert markdown headings
        Args:
            read_file: file to read
    """
    with open(read_file, 'r') as markdown, open(write_file, 'w') as html:
        for line in markdown:
            if line.startswith('# '):
                line = '<h1>' + line[2:] + '</h1>'
            elif line.startswith('## '):
                line = '<h2>' + line[3:] + '</h2>'
            elif line.startswith('### '):
                line = '<h3>' + line[4:] + '</h3>'
            elif line.startswith('#### '):
                line = '<h4>' + line[5:] + '</h4>'
            elif line.startswith('##### '):
                line = '<h5>' + line[6:] + '</h5>'
            elif line.startswith('###### '):
                line = '<h6>' + line[7:] + '</h6>'

            html.write(line)


if __name__ == "__main__":
    if len(argv) < 2:
        stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    if not path.isfile(argv[1]):
        stderr.write("Missing {}\n".format(argv[1]))
        exit(1)

    headings(argv[1], argv[2])
