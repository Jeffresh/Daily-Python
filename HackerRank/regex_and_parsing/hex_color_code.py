# You are given lines of CSS code.
# Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.

# Input Format
#
# The first line contains
# N the number of code lines.
# The next lines contains CSS Codes.

import re

if __name__ == '__main__':
    line_number = int(input())
    regex = '(?<!^)#(?:[\dA-Fa-f]{3}){1,2}'

    for _ in range(line_number):
        css_code = input()
        colors = re.findall(regex, css_code)
        if colors:
            print(*colors, sep='\n')
