# task
# You are given two sets a and b .
# Your job is to find whether set a is a subset of set b .
#
# If set a is subset of set b , print True.
# If set a is not a subset of set b , print False.

# Input Format
#
# The first line will contain the number of test cases,
# .
# The first line of each test case contains the number of elements in set a.
# The second line of each test case contains the space separated elements of set a .
# The third line of each test case contains the number of elements in set b .
# The fourth line of each test case contains the space separated elements of set b .

if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        size_a = int(input())
        set_a = set(map(int, input().split()))
        size_b = int(input())
        set_b = set(map(int, input().split()))

        print(abs(size_a - size_b) == len(set_b.difference(set_a)))
