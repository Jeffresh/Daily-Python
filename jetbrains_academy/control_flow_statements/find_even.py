# Write a program that prints all positive even numbers less than the input number using the while loop.
#
# The input format:
#
# The maximum number N that varies from 1 to 200.
#
# The output format:
#
# All positive even numbers less than N in ascending order. Each number must be on a separate line.

def count_evens(upper_limit):
    for i in range(2, upper_limit, 2):
        print(i)


if __name__ == '__main__':
    number = int(input())
    count_evens(number)
