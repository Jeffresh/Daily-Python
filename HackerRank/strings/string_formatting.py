# Given an integer, n , print the following values for each integer i from 1 to n :
# 1. Decimal
# 2. Octal
# 3. Hexadecimal (capitalized)
# 4. Binary
#
# The four values must be printed on a single line in the order specified above for each i
# from 1 to n . Each value should be space-padded to match the width of the binary value of n.


def print_formatted(number):
    width = len("{0:b}".format(number))
    output = [
        '{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i, width=width) for
        i in range(1, number + 1)]

    print('\n'.join(output))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
