# Task
#
# You are given a string.
# Your task is to find the first occurrence of an alphanumeric character in
# (read from left to right) that has consecutive repetitions.

import re

if __name__ == '__main__':
    string = input()
    m = re.search(r'(\w)\1', string)
    print(m.group(1))
