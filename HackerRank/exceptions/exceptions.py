# Task
#
# You are given two values a and b,
# Perform integer division and print a/b.

# Input Format
#
# The first line contains T, the number of test cases.
# The next T lines each contain the space separated values of a and b.

if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        try:
            a, b = map(int, input().split())
            print(a // b)
        except (ZeroDivisionError, ValueError) as error:
            print("Error Code:", error)

