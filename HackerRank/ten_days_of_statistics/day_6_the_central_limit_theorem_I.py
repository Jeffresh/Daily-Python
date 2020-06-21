# Task A large elevator can transport a maximum 9800 of pounds. Suppose a load of cargo containing 49 boxes must be
# transported via the elevator. The box weight of this type of cargo follows a distribution with a mean of pounds 205
# and a standard deviation of 15 pounds. Based on this information, what is the probability that all 49 boxes can be
# safely loaded into the freight elevator and transported?

from math import erf, sqrt


def cumulative_probability_normal_distribution(mean, std, x):
    return (1 + erf((x - mean) / (std * sqrt(2)))) * 0.5


if __name__ == '__main__':
    maximum_pounds = 9800
    max_cargo = 49
    mean = 205
    std = 15

    mu_sum = max_cargo * mean
    std_sum = sqrt(max_cargo) * std

    pr = (round(cumulative_probability_normal_distribution(mu_sum, std_sum, maximum_pounds), 4))

    print(pr)
