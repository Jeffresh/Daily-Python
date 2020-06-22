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
    rx = [sorted(data).index(x) for x in data]
    return rx


def has_duplicates(data):
    for x in data:
        if data.count(x) > 1:
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


def pearson_correlation_coefficient(dataset_x, dataset_y):
    n = len(dataset_x)
    mean_x = round(mean(dataset_x, size_datasets), 2)
    mean_y = round(mean(dataset_y, size_datasets), 2)
    std_x = std(dataset_x, mean_x, size_datasets)
    std_y = std(dataset_y, mean_y, size_datasets)

    covariance_value = covariance(dataset_x, dataset_y, mean_x, mean_y)
    return covariance_value / (n * std_x * std_y)


def spearman_rank_correlation_coefficient(dataset_x, dataset_y):
    sprcc = pearson_correlation_coefficient(rank_x, rank_y)

    return sprcc


def spearman_rank_correlation_coefficient_no_duplicates(rank_x, rank_y):
    n = len(rank_x)
    diff_sum = sum([(x - y) ** 2 for x, y in zip(rank_x, rank_y)])
    sprcc = 1 - ((6 * diff_sum) / (n * (n ** 2 - 1)))
    return sprcc


if __name__ == '__main__':
    size_datasets = float(input())
    dataset_x = list(map(float, input().split()))
    dataset_y = list(map(float, input().split()))

    rank_x = rank(dataset_x)
    rank_y = rank(dataset_y)

    if has_duplicates(dataset_x) or has_duplicates(dataset_y):
        sprcc = spearman_rank_correlation_coefficient(rank_x, rank_y)
        print(round(sprcc, 3))
    else:
        sprcc = spearman_rank_correlation_coefficient_no_duplicates(rank_x, rank_y)

    print(sprcc)
