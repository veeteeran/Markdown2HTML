#!/usr/bin/python3
"""Check for proper number of args"""
from os import path
from sys import argv, stderr

def headings(markdown="", html=""):
    """
    Convert markdown headings
        Args:
            markdown: file to read
            html: file to write
    """
    if markdown == "" or html == "":
        return

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
    """
    Convert markdown unordered list
        Args:
            markdown: file to read
            html: file to write
    """
    if markdown == "" or html == "":
        return

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
        if list_open:
            h.write('</ul>')

def ordered(markdown="", html=""):
    """
    Convert markdown ordered list
        Args:
            markdown: file to read
            html: file to write
    """
    if markdown == "" or html == "":
        return

    with open(markdown, 'r') as m, open(html, 'a') as h:
        list_open = False
        for line in m:
            if not line.startswith('* '):
                list_open = False
                continue

            if line.startswith('* ') and not list_open:
                line = '<ol><li>' + line[2:] + '</li>'
                list_open = True
            elif line.startswith('* '):
                line = '<li>' + line[2:] + '</li>'
            h.write(line)
        h.write('</ol>')

# def paragraphs(markdown="", html=""):
#     """
#     Convert markdown paragraphs
#         Args:
#             markdown: file to read
#             html: file to write
#     """
#     with open(markdown, 'r') as m, open(html, 'a') as h:
#         line_start = False
#         for line in m:
#             if not line[0].isalpha():
#                 line_start = False
#                 continue

#             if line[0].isalpha() and not line_start:
#                 line = '<p>' + line
#                 line_start = True

#             if line == '\n':

if __name__ == "__main__":
    if len(argv) < 2:
        stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    if not path.isfile(argv[1]):
        stderr.write("Missing {}\n".format(argv[1]))
        exit(1)

    headings(argv[1], argv[2])
    unordered(argv[1], argv[2])
    ordered(argv[1], argv[2])
