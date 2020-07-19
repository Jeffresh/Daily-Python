# Read a string with digits from the input and convert each number to an integer.
# Include only odd digits in your list and print what you'll get.

if __name__ == '__main__':
    digits = input()
    print([int(x) for x in digits if int(x) % 2 == 1])
