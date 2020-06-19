# Task
# The probability that a machine produces a defective product is 1/3 .
# What is the probability that the 1st defect is found during the first 5 inspections?
from math import factorial


def combination(n, x):
    return factorial(n) / factorial(x) / factorial(n - x)


def geometric_distribution(n, p):
    q = 1 - p
    return q ** (n - 1) * p


def negative_binomial(n, x, p):
    return combination(n - 1, x - 1) * pow(p, x) * pow(1 - p, n - x)


if __name__ == "__main__":
    nume, deno = map(float, input().split())
    n = float(input())
    p_defect = nume / deno
    p_not_defetc = 1 - p_defect

    p_first_5th_not_defect = negative_binomial(5, 5, p_not_defetc)

    print('{0:.03f}'.format(1 - p_first_5th_not_defect))
