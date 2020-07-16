# Task
#
# You are given a 2-D array with dimensions N X M.
# Your task is to perform the min function over axis and then find the max of that.

# Input Format
#
# The first line of input contains the space separated values of N and M
# The next lines contains space separated integers.
import numpy as np

if __name__ == '__main__':
    n, m = list(map(int, input().split()))

    matrix_a = np.array([input().split() for _ in range(n)], int)
    min_values = np.min(matrix_a, axis=1)
    max_value = np.max(min_values)

    print(max_value)
