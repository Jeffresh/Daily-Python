# ABCXYZ company has up to 100 employees.
#
# The company decides to create a unique identification number (UID) for each of its employees.
# The company has assigned you the task of validating all the randomly generated UIDs.
#
# A valid UID must follow the rules below:
#
# It must contain at least 2 uppercase English alphabet characters.

# It must contain at least digits ( 0 - 9)

# It should only contain alphanumeric characters (a - z, A - Z & 0 - 9)

# No character should repeat.
# There must be exactly 10 characters in a valid UID.


# Input Format
#
# The first line contains an integer T the number of test cases.
# The next T lines contains an employee's UID.

import re


def check_id(uid):
    no_repeats = r"(?!.*(.).*\1)"
    two_or_more_upper = r"(?=(?:.*[A-Z]){2,})"
    three_or_more_digits = r"(?=(?:.*\d){3,})"
    ten_alphanumerics = r"[a-zA-Z0-9]{10}"
    filters = no_repeats, two_or_more_upper, three_or_more_digits, ten_alphanumerics

    valid = all([re.match(filter_, uid) for filter_ in filters])
    if valid:
        print("Valid")
    else:
        print("Invalid")


if __name__ == '__main__':

    id_numbers = int(input())
    for _ in range(id_numbers):
        id = input()
        check_id(id)
