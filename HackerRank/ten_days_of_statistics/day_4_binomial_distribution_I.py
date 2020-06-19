# Task
# The ratio of boys to girls for babies born in Russia is  1.09:1. If there is
# child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

# Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of
# decimal places (i.e., format).

from math import factorial


def combination(n, x):
    return factorial(n) / factorial(x) / factorial(n - x)


def binomial(x, n, p):
    return combination(n, x) * pow(p, x) * pow(1 - p, n - x)


if __name__ == "__main__":

    boys_ratio = 1.09
    not_boy_ratio = 1

    result = sum([binomial(6, i, boys_ratio / (boys_ratio + not_boy_ratio)) for i in range(3, 7)])
    print('{0:.03f}'.format(result))


