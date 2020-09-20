# Write a program that reads from the console integers (one in a line) until their sum is equal to 0.
# Immediately after that, it should display the sum of the squares of all the entered numbers.
#
# It is guaranteed that at some point the sum of the entered numbers will be equal to 0. After that, you should stop
# reading the input.
#
# You only need to output the sum of the squares once. Don't output it every time after reading an
# integer from the input.
#
# In case the first integer equals to 0, just print out 0 instead of the sum of the squares.
#
# For example, we are reading the numbers 1, -3, 5, -6, -10, 13. At this point, we have noticed that the sum of these
# numbers is 0 and output the sum of their squares, not paying attention to the fact that there are still unread values.


if __name__ == '__main__':
    numbers = [int(input())]

    while sum(numbers):
        numbers.append(int(input()))
    print(sum(map(lambda x: x ** 2, numbers)))
