# Advanced input() handling is used to read input directly into several variables, for example:
#
# x, y = input().split()
#
# Use it to print the next message with the two input values: "x of y"

if __name__ == '__main__':
    x, y = input().split()
    print(' of '.join([x, y]))