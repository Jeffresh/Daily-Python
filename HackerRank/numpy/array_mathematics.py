# Task
#
# You are given two integer arrays,
# A and B of dimensions N X M.
# Your task is to perform the following operations:
#
# Add ( A + B)
# Subtract ( A - B )
# Multiply ( A * B )
# Integer Division ( A / B)
# Mod ( A % B)
# Power ( A ** B)

# Input Format
#
# The first line contains two space separated integers, N and M.
# The next N lines contains M space separated integers of array A.
# The following N lines contains M space separated integers of array B.
import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    array_a = np.array([input().split() for _ in range(n)], int)
    array_b = np.array([input().split() for _ in range(n)], int)

    print(array_a + array_b)
    print(array_a - array_b)
    print(array_a * array_b)
    print(array_a // array_b)
    print(array_a % array_b)
    print(array_a ** array_b)
