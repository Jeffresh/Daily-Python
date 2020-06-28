# Task
# Read in two integers, and , and print three lines.
# The first line is the integer division (While using Python2 remember to import division from __future__).
# The second line is the result of the modulo operator: .
# The third line prints the divmod of and .

if __name__ == '__main__':
    integer_a = int(input())
    integer_b = int(input())

    integer_division = integer_a // integer_b
    reminder = integer_a % integer_b
    division_and_reminder = divmod(integer_a, integer_b)

    print(integer_division)
    print(reminder)
    print(division_and_reminder)

