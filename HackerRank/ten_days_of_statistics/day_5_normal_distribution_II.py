# Task

# The final grades for a Physics exam taken by a large group of students have a mean 70 of
# and a standard deviation of 10
#
# If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:
#
# 1. Scored higher than 80
# 2. Passed the test ( grade >= 60)
# 3. Failed the test ( grade < 60)
#
# Find and print the answer to each question on a new line, rounded to a scale of 2 decimal places.

from math import sqrt, pi, exp, erf


def normal_distribution(mean, std, x):
    return (1 / (std * sqrt(2 * pi))) * exp((- (x - mean) ** 2) / (2 * std ** 2))


def cumulative_probability_normal_distribution(mean, std, x):
    return (1 + erf((x - mean) / (std * sqrt(2)))) / 2


if __name__ == '__main__':
    normal_mean, normal_std = map(float, input().split())
    grade_to_higher = float(input())
    grade_to_pass = float(input())
