# Task
# A group of five students enrolls in Statistics immediately after taking a Math aptitude test.
# Each student's Math aptitude test score, x, and Statistics course grade, y,
# can be expressed as the following list of (x,y) points.
# Determine the equation of the best-fit line using the least squares method, then compute and print the value of y
# when x = 80.

from math import sqrt


def mean(data):
    size = len(data)
    return sum(data) / size


def std(data):
    size = len(data)
    mean_ = mean(data)
    square_distances = [(x - mean_) ** 2 for x in data]
    variance = sum(square_distances) / size
    std = sqrt(variance)
    return std


def covariance(dataset_x, dataset_y, mean_x, mean_y):
    covariance_value = sum([(i - mean_x) * (j - mean_y) for i, j in zip(dataset_x, dataset_y)])
    return covariance_value


def pearson_correlation_coefficient(dataset_x, dataset_y):
    n = len(dataset_x)
    mean_x = round(mean(dataset_x), 2)
    mean_y = round(mean(dataset_y), 2)
    std_x = std(dataset_x)
    std_y = std(dataset_y)

    covariance_value = covariance(dataset_x, dataset_y, mean_x, mean_y)
    return covariance_value / (n * std_x * std_y)


def linear_regression(x, y, evalue):
    b = pearson_correlation_coefficient(x, y) * (std(y) / std(x))
    a = mean(y) - b * mean(x)

    estimation = a + b * evalue
    return estimation


if __name__ == '__main__':
    x, y = [], []
    for _ in range(5):
        i = input().split()
        x.append(int(i[0]))
        y.append(int(i[1]))

    predict_value = 80
    predicted = linear_regression(x, y, 80)
    print(round(predicted, 3))