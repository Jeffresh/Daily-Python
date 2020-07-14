# Task
#
# You are given a space separated list of nine integers. Your task is to
# convert this list into a 3 x 3 NumPy array.


# Input Format
#
# A single line of input  9
# space separated integers.
import numpy as np

if __name__ == '__main__':
    list_numbers = input().split()
    numpy_array = np.array(list_numbers, int)

    matrix_a = numpy_array.reshape(3, 3)
    print(matrix_a)
