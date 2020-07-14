# Task
#
# You are given a space separated list of numbers.
# Your task is to print a reversed NumPy array with the element type float.

# Input Format
#
# A single line of input containing space separated numbers.


import numpy as np


def arrays(arr):
    return np.array(arr, float)[::-1]


if __name__ == '__main__':
    number_list = input().split()
    result = arrays(number_list)
    print(result)
