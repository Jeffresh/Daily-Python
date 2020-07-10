# Task
# Given n pairs of names and email addresses as input, print each name and email address pair having a
# valid email address on a new line.

# Input Format
#
# The first line contains a single integer, n , denoting the number of email address.
# Each line i of the n subsequent lines contains a name and an email address
# as two space-separated values following this format:
# name <user@email.com>

import re

if __name__ == '__main__':
    addresses_number = int(input())
    regex = '<[A-Za-z][\w._-]+@[A-Za-z]+\.[A-Za-z]{1,3}>'

    for _ in range(addresses_number):
        name, address = input().split(" ")
        if re.match(regex, str(address)):
            print('{} {}'.format(name, address))
