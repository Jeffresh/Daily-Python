# Task
# The manager of a industrial plant is planning to buy a machine of either type A or type B.
#
# For each day’s operation:
#
# The number of repairs X, that machine A needs is a Poisson random variable with mean 0.88 .
# The daily cost of operating A is CA = 160 + 40 X^2 .

# The number of repairs Y, that machine B needs is a Poisson random variable with mean 1.55 .
# The daily cost of operating B is CB = 128 + 40 Y^2 .
#


if __name__ == "__main__":
    mean_a, mean_b = map(float, input().split())

    CA = 160 + 40 * (mean_a + mean_a ** 2)
    CB = 128 + 40 * (mean_b + mean_b ** 2)
    print('{0:.03f}'.format(CA))
    print('{0:.03f}'.format(CB))
