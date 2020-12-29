#!/usr/bin/python3
"""Check for proper number of args"""
from os import path
import re
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
    if not line.startswith('# '):
        return line

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

    return line

def unordered(line, ul_open):
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
    """
    Combines code for functions above
    """
    check_args(args[0])
    markdown = args[0][1]
    html = args[0][2]
    with open(markdown, 'r') as m, open(html, 'a') as h:
        ul_open = False
        ol_open = False
        p_open = False
        for line in m:
            # Headings
#            line = headings(line)
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

            # Unordered lists
            if line.startswith('- ') and not ul_open:
                line = '<ul><li>' + line[2:] + '</li>'
                ul_open = True
            elif line.startswith('- '):
                line = '<li>' + line[2:] + '</li>'

            if line == '\n' and ul_open:
                h.write('</ul>')
                ul_open = False

            # Ordered lists
            if line.startswith('* ') and not ol_open:
                line = '<ol><li>' + line[2:] + '</li>'
                ol_open = True
            elif line.startswith('* '):
                line = '<li>' + line[2:] + '</li>'

#            h.write(line)

            if line == '\n' and ol_open:
                h.write('</ol>')
                ol_open = False

            bold = line[0] == '*'
            em = line[0] == '_'
            if (line[0].isalpha() or bold or em) and not p_open:
                line = '<p>' + line[0:]
                p_open = True

            if line == '\n' and p_open:
                h.write('</p>')
                p_open = False

            if line[0].isalpha() and p_open:
                line = '<br/>' + line[0:]

            if '**' in line:
                pattern = '([**]).+([**])'
                x = re.search(pattern, line)
                find = x.group()
                replace = find.strip('*')
                replace = '<b>' + replace + '</b>'
                line = line.replace(find, replace)
                
            if '__' in line:
                pattern = '([__]).+([__])'
                x = re.search(pattern, line)
                find = x.group()
                replace = find.strip('_')
                replace = '<em>' + replace + '</em>'
                line = line.replace(find, replace)

            h.write(line)

        # Close lists
        if ul_open:
            h.write('</ul>')

        if ol_open:
            h.write('</ol>')

        # Close paragraphs
        if p_open:
            h.write('</p>')

if __name__ == "__main__":

    convert(argv)
#    check_args(argv)
#    headings(argv[1], argv[2])
#    unordered(argv[1], argv[2])
#    ordered(argv[1], argv[2])
#    paragraphs(argv[1], argv[2])
