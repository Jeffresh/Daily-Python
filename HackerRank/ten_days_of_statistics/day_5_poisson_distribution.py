# Task
# A random variable X , follows Poisson distribution with mean of 2.5
# Find the probability with which the random variable X is equal to 5.

from math import factorial


def poisson_distribution(k, mean):
    return (mean ** k * 2.71828 ** (-mean)) / factorial(k)


if __name__ == "__main__":
    mean = float(input())
    variable_value = float(input())

    p = poisson_distribution(variable_value, mean)

    print('{0:.03f}'.format(p))
