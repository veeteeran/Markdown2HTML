#!/usr/bin/python3
"""Check for proper number of args"""
from os import path
from sys import argv, stderr

def headings(markdown="", html=""):
    """
    Convert markdown headings
        Args:
            markdown: file to read
    """
    with open(markdown, 'r') as m, open(html, 'a') as h:
        for line in m:
            if not line.startswith('#'):
                continue

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

            h.write(line)

def unordered(markdown="", html=""):
    with open(markdown, 'r') as m, open(html, 'a') as h:
        list_open = False
        for line in m:
            if not line.startswith('- '):
                list_open = False
                continue

            if line.startswith('- ') and not list_open:
                line = '<ul><li>' + line[2:] + '</li>'
                list_open = True
            elif line.startswith('- '):
                line = '<li>' + line[2:] + '</li>'
            h.write(line)
        h.write('</ul>')

if __name__ == "__main__":
    if len(argv) < 2:
        stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    if not path.isfile(argv[1]):
        stderr.write("Missing {}\n".format(argv[1]))
        exit(1)

    headings(argv[1], argv[2])
    unordered(argv[1], argv[2])
