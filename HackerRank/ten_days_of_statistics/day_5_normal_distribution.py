# Task
# In a certain plant, the time taken to assemble a car is a random variable, X
# having a normal distribution with a mean 20 of hours and a standard deviation of
# 2 hours. What is the probability that a car can be assembled at this plant in:

# Less than 19.5 hours?
# Between 20 and 22 hours?

from math import sqrt, pi, exp, erf


def normal_distribution(mean, std, x):
    return (1 / (std * sqrt(2 * pi))) * exp((- (x - mean) ** 2) / (2 * std ** 2))


def cumulative_probability_normal_distribution(mean, std, x):
    return (1 + erf((x - mean) / (std * sqrt(2))))/2


if __name__ == '__main__':
    normal_mean, normal_std = map(float, input().split())
    value = float(input())
    range_a, range_b = map(float, input().split())

    # P less than 19.5
    p_lt = cumulative_probability_normal_distribution(normal_mean, normal_std, value)
    print('{0:.03f}'.format(p_lt))

    #P between 20 22
    p_range_a = cumulative_probability_normal_distribution(normal_mean, normal_std, range_a)
    p_range_b = cumulative_probability_normal_distribution(normal_mean, normal_std, range_b)
    p_range = p_range_b - p_range_a
    print('{0:.03f}'.format(p_range))

