# Task
#
# Your task is to print an array of size
# X with its main diagonal elements as 's and 's everywhere else.
#
# Input Format
#
# A single line containing the space separated values of N and M
# N denotes the rows.
# M denotes the columns

import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())

    matrix_diagonal = np.identity(n) if n == m else np.eye(n, m)
    print(matrix_diagonal)
