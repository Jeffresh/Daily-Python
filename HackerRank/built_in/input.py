# Task
#
# You are given a polynomial P of a single indeterminate (or variable), x .
# You are also given the values of x and k . Your task is to verify if P(x) = k .

# Input Format
#
# The first line contains the space separated values of x and k
# The second line contains the polynomial P .

if __name__ == '__main__':
    x, k = map(int, input().split())
    print(eval(input()) == k)
