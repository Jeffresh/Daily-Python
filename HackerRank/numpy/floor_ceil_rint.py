# Task
# You are given a 1-D array, A .
# Your task is to print the  floor, ceil, and rint of all the elements of A.

# Input Format
#
# A single line of input containing the space separated elements of array A.
import numpy as np

if __name__ == '__main__':
    number_list = input().split()
    array_1d = np.array(number_list, float)
    print(np.floor(array_1d), np.ceil(array_1d), np.rint(array_1d), sep='\n')
