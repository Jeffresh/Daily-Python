# Write a program that converts a given list into a list with binary values:
# either 1 or 0. If the number in the initial list was greater than 0,
# in the binary list there should be 1, and if the number was less or equal,
# in the new list you should write 0. Naturally, use the list comprehension and print the result.
#
# Input format: a list with integer numbers, e.g. [5, 0, 4, -10].
#
# Output format: a list consisting of ones and zeros, e.g. [1, 0, 1, 0].

if __name__ == '__main__':
    # the following line reads the list from the input, do not modify it, please
    old_list = [int(num) for num in input().split()]

    binary_list = [1 if x > 0 else 0 for x in old_list]
    print(binary_list)