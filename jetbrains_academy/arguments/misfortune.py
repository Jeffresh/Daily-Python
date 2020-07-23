# Robin has declared a function that prints the squares of odd numbers in the specified range.
# Unfortunately, several function calls gave an unexpected result. The function itself seems to be fine.
# Help Robin figure out what went wrong in these calls and fix them.


def square_odds(a, b):
    start = a
    if a % 2 == 0:
        start += 1
    end = b + 1
    for odd in range(start, end, 2):
        print(odd ** 2)


if __name__ == '__main__':
    # from 22 to 42
    square_odds(a=22, b=42)

    # from 15 to 31
    square_odds(15, 31)

    # from 42 to 49
    square_odds(b=49, a=42)
