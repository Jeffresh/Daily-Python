# Task

# You are given two integer arrays of size N x P ans M x P ( N & M are rows, and P is the column).
# Your task is to concatenate the arrays along axis 0

# Input Format
#
# The first line contains space separated integers N, M and  P.
# The next N lines contains the space separated elements of the P columns.
# After that, the next M lines contains the space separated elements of the P columns.
import numpy as np

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    matrix_a = np.array([input().split() for _ in range(n)], int)
    matrix_b = np.array([input().split() for _ in range(m)], int)

    print(np.concatenate((matrix_a, matrix_b), axis=0))
