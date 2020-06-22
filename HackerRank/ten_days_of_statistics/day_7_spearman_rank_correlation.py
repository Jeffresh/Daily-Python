# Task
# Given two n -element data sets, X and Y calculate the value of Spearman's rank correlation coefficient.
#
# Input Format
#
# The first line contains an integer, n , denoting the number of values in data sets X and Y .
# The second line contains n space-separated real numbers (scaled to at most one decimal place) denoting data set X.
# The third line contains n space-separated real numbers (scaled to at most one decimal place) denoting data set Y .

# rs (spearman rank correlation coefficient) is equal to Pearson correlation coefficient of Rankx and Ranky.
# rank is equal of the order on the list.
# Special case if X and Y dont contain duplicates then rs = 1- (6 * sum(rankxi - rankxj))/(n*n^2 -1)

from math import sqrt


def rank(data):
    rx = [sorted(x).index(x) for x in data]
    return rx


def has_duplicates(data):
    for x in data:
        if (data.count(x) > 1):
            return True
    return False


def mean(data, size):
    return sum(data) / size


def std(data, mean, size):
    square_distances = [(x - mean) ** 2 for x in data]
    variance = sum(square_distances) / size
    std = sqrt(variance)
    return std


def covariance(dataset_x, dataset_y, mean_x, mean_y):
    covariance_value = sum([(i - mean_x) * (j - mean_y) for i, j in zip(dataset_x, dataset_y)])
    return covariance_value


def pearson_correlation_coefficient(covariance_value, std_x, std_y, n):
    return covariance_value / (n * std_x * std_y)


if __name__ == '__main__':
    pass
