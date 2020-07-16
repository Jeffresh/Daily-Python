# Task
#
# You are given two arrays A and B . Both have de dimensions of N x N
#
# Your task is to compute their matrix product.
#
# Input Format
#
# The first line contains the integer N
# The next N lines contains N space separated integers of array A.
# The following N lines contains N space separated integers of array B.
import numpy as np

if __name__ == '__main__':
    n = int(input())

    mat_a = np.array([input().split() for _ in range(n)], int)
    mat_b = np.array([input().split() for _ in range(n)], int)

    print(np.dot(mat_a, mat_b))


