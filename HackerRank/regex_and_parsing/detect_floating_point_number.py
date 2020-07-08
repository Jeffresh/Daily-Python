# You are given a string .
# Your task is to verify that
#
# is a floating point number.
#
# In this task, a valid float number must satisfy all of the following requirements:

# Number can start with +, - or . symbol.

# Nubmer must contain at least 1 decimal value.
# Number must have exactle one . symbol
# Number must not give any exceptions when converted using float(N)


# Input Format
#
# The first line contains an integer T , the number of test cases.
# The next T line(s) contains a string N.
import re

if __name__ == '__main__':
    number_cases = int(input())

    for _ in range(number_cases):
        number = input()
        print(re.match('^[+-]?\d*\.\d+$', number))
