# Task
#
# You are given a 2-D array of size N x M
#
#
# Your task is to find:
#
# 1. The mean along axis 1
#
# 2. The var along axis 0
# 3. The std along axis None
#
# Input Format
#
# The first line contains the space separated values of N and M
# The next N lines contains M space separated integers.
import numpy as np

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    mat_a = np.array([input().split() for _ in range(n)], int)

    print(np.mean(mat_a, axis=1))
    print(np.var(mat_a, axis=0))
    print(np.std(mat_a))


