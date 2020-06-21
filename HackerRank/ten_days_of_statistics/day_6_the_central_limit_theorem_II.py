# Task
# The number of tickets purchased by each student for the University X vs.
# University Y football game follows a distribution that has a mean 24 of and a standard deviation of 2.0
# A few hours before the game starts, 100 eager students line up to purchase last-minute tickets.
# If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?

from math import erf, sqrt


def cumulative_probability_normal_distribution(mean, std, x):
    return (1 + erf((x - mean) / (std * sqrt(2)))) * 0.5


if __name__ == '__main__':
    max_tickets = 250
    students = 100
    mean_sells = 2.4
    std_sells = 2.0

    sum_mean = students * mean_sells
    sum_std = sqrt(students) * std_sells

    pr = cumulative_probability_normal_distribution(sum_mean, sum_std, max_tickets)
    print('{0:.04f}'.format(pr))
