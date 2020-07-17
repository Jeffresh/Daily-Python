# Task
# You are given a square matrix A with dimensions N x N. Your task is to find the determinant.
# Note: Round the answer to2 places after the decimal.

# Input format
# the first line contains the integer N.
# Then ext N lines contains the N space separated elements of array A.
import numpy as np

if __name__ == '__main__':
    n = int(input())
    mat_a = np.array([input().split() for _ in range(n)], float)
    print(round(np.linalg.det(mat_a), 2))
