# Task
# The probability that a machine produces a defective product is 1/3.
# What is the probability that the 1st defect is found during the 5th inspection?


def geometric_distribution(n, p):
    q = 1 - p
    return q ** (n - 1) * p


if __name__ == "__main__":
    nume, deno = map(float, input().split())
    n = float(input())
    p_defect = nume / deno
    print('{0:.03f}'.format(geometric_distribution(n, p_defect)))
