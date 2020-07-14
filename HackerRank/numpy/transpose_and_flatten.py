# Task
#
# You are given a N X N integer array matrix with space separated elements ( = rows and = columns).
# Your task is to print the transpose and flatten results.
#
# Input Format
#
# The first line contains the space separated values of N and M.
# The next N lines contains the space separated elements of M columns.

import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix_list = [list(map(int, input().split())) for _ in range(n)]
    matrix_a = np.array(matrix_list)

    matrix_a_transposed = matrix_a.transpose()
    matrix_flatten = matrix_a.flatten()

    print(matrix_a_transposed)
    print(matrix_flatten)
