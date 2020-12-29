#!/usr/bin/python3
"""Check for proper number of args"""
from os import path
from sys import argv, stderr


def check_args(*args):
    """
    Check input for proper number of args 
    """
    for arg in args:
        if len(arg) < 2:
            stderr.write("Usage: ./markdown2html.py README.md README.html\n")
            exit(1)
        else:
            if not path.isfile(arg[1]):
                stderr.write("Missing {}\n".format(arg[1]))
                exit(1)

def headings(line):
    """
    Convert markdown headings
        Args:
            markdown: file to read
            html: file to write
    """
    list_open = False

    if not line.startswith('#'):
        return

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

def unordered(line):
    """
    Convert markdown unordered list
        Args:
            markdown: file to read
            html: file to write
    """
    list_open = False

    if not line.startswith('- '):
        return

    if line.startswith('- ') and not list_open:
        line = '<ul><li>' + line[2:] + '</li>'
        list_open = True
    elif line.startswith('- '):
        line = '<li>' + line[2:] + '</li>'

    h.write(line)

    if line == '\n' and list_open:
        h.write('</ul>')
        list_open = False

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

def paragraphs(markdown="", html=""):
    """
    Convert markdown paragraphs
        Args:
            markdown: file to read
            html: file to write
    """
    with open(markdown, 'r') as m, open(html, 'a') as h:
        line_start = False
        for line in m:
            if line == '\n' and line_start:
                h.write('</p>')
                continue

            if not line[0].isalpha():
                line_start = False
                print('Not simple text')

#             if line[0].isalpha() and not line_start:
#                 line = '<p>' + line
#                 line_start = True

def convert(*args):
    check_args(args[0])
    markdown = args[0][1]
    html = args[0][2]
    with open(markdown, 'r') as m, open(html, 'a') as h:
        list_open = False
        for line in m:
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

            if line.startswith('- ') and not list_open:
                line = '<ul><li>' + line[2:] + '</li>'
                list_open = True
            elif line.startswith('- '):
                line = '<li>' + line[2:] + '</li>'

            h.write(line)

            if line == '\n' and list_open:
                h.write('</ul>')
                list_open = False

        if list_open:
            h.write('</ul>')

if __name__ == "__main__":

    convert(argv)
#    check_args(argv)
#    headings(argv[1], argv[2])
#    unordered(argv[1], argv[2])
#    ordered(argv[1], argv[2])
#    paragraphs(argv[1], argv[2])
