# A manufacturer of metal pistons finds that, on average,
# 12% of the pistons they manufacture are rejected because they are incorrectly sized.
# What is the probability that a batch of 10 pistons will contain:
#
# No more than 2 rejects?
# At least 2 rejects?

from math import factorial


def combination(n, x):
    return factorial(n) / factorial(x) / factorial(n - x)


def binomial(x, n, p):
    return combination(n, x) * pow(p, x) * pow(1 - p, n - x)


if __name__ == "__main__":

    rejected_percentage = 12
    batch_size = 10

    p_rejected = ((batch_size * rejected_percentage)/100)/10

    result = sum([binomial(10, i, p_rejected) for i in range(3)])
    print('{0:.03f}'.format(result))

    result = sum([binomial(10, i, p_rejected) for i in range(2, 11)])
    print('{0:.03f}'.format(result))




