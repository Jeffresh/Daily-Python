# Write a function called multiply that takes a changeable number of arguments and returns their product.
#
# Assume that only integer numbers are to be passed into the function.
#
# Given only one integer number, multiply it by 1. Thus, the product will be equal to this integer.
#
# You are not supposed to call the function, simply implement it.
from functools import reduce


def multiply(*args):
    return reduce(lambda x, y: x * y, args)


if __name__ == '__main__':
    print(multiply(8))
