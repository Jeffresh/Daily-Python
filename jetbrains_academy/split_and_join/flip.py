# Let's try to reverse a numeric sequence. Read it from the input and print its
# numbers in reverse order separated by spaces.

if __name__ == '__main__':
    list_number = input().split()
    print(' '.join(list_number[::-1]))
