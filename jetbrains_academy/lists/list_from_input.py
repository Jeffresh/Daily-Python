# Write a program that takes n numbers as input, creates a list from them and then prints it.
#
# The first input line is n – length of the resulting list. It is followed by n lines containing list elements.

if __name__ == '__main__':
    n = int(input())
    numbers = []
    for _i in range(n):
        numbers.append(int(input()))
    print(numbers)
