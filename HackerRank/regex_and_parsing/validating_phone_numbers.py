# Task

# You are given some input, and you are required to check whether they are valid mobile numbers.
#
# A valid mobile number is a ten digit number starting with a 7, 8 , 9.

# Input Format
#
# The first line contains an integer N the number of inputs.
# N lines follow, each containing some string.

import re

if __name__ == '__main__':
    phone_numbers = int(input())
    regex = '^[789]\d{9}'

    for _ in range(phone_numbers):
        number = input()
        if re.match(regex, number):
            print('YES')
        else:
            print('NO')

