# Task
#
# You are given a text of
#
# lines. The text contains && and || symbols.
# Your task is to modify those symbols to the following:
#
# && → and
# || → or
#
# Both && and || should have a space " " on both sides.
import re

if __name__ == '__main__':
    line_number = int(input())
    regex = '(?<= )(&&|\|\|)(?= )'

    for _ in range(line_number):
        line = input()
        print(re.sub(regex, lambda x: 'and' if x.group() == '&&' else 'or', line))
