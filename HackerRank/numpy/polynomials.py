# Task
#
# You are given the coefficients of a polynomial P
# Your task is to find the value of P at point x .

# Input Format
#
# The first line contains the space separated value of the coefficients in P.
# The second line contains the value of x.
import numpy as np

if __name__ == '__main__':
    coeffs = np.array(input().split(), float)
    point = float(input())
    value = np.polyval(coeffs, point)
    print(value)
