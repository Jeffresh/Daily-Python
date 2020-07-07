# Task
# You are given a string S .
# S contains alphanumeric characters only.
#
# Your task is to sort the string S
#
# in the following manner:
#
#     All sorted lowercase letters are ahead of uppercase letters.
#     All sorted uppercase letters are ahead of digits.
#     All sorted odd digits are ahead of sorted even digits.

import string

if __name__ == '__main__':
    print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')
