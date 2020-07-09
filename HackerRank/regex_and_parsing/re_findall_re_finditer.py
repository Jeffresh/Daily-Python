# Task
# You are given a string S . It consists of alphanumeric characters, spaces and symbols(+,-).
# Your task is to find all the substrings of S that contains 2 or more vowels.
# Also, these substrings must lie in between 2 consonants and should contain vowels only.


import re

if __name__ == '__main__':
    CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
    regex = '(?<=[' + CONSONANTS + '])([aeiou]{2,})[' + CONSONANTS + ']'

    string = input()

    match = re.findall(regex, string, re.IGNORECASE)

    print(*match if match else [-1], sep='\n')
