# Task
#
# You are given the shape of the array in the form of space-separated integers,
# each integer representing the size of different dimensions,
# your task is to print an array of the given shape and integer type using the tools
# numpy.zeros and numpy.ones.


# Input Format
#
# A single line containing the space-separated integers.
import numpy as np

if __name__ == '__main__':
    dimension_list = list(map(int, input().split()))

    matrices_zero = np.zeros(dimension_list, dtype=int)
    matrices_one = np.ones(dimension_list, dtype=int)

    print(matrices_zero, matrices_one, sep='\n')
