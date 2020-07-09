# Task
# You are given a string S .
# Your task is to find the indices of the start and end of string K in S.

# Input Format
#
# The first line contains the string S.
# The second line contains the string k.

import re

if __name__ == '__main__':

    S = input()
    k = input()

    found = False
    for m in re.finditer(r'(?=(' + k + '))', S):
        found = True
        print((m.start(1), m.end(1) - 1))
    if found:
        print((-1, -1))
