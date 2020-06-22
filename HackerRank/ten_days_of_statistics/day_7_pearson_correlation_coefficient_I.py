from math import sqrt


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
    size_datasets = float(input())
    dataset_x = list(map(float, input().split()))
    dataset_y = list(map(float, input().split()))

    mean_x = round(mean(dataset_x, size_datasets), 2)
    mean_y = round(mean(dataset_y, size_datasets), 2)
    std_x = std(dataset_x, mean_x, size_datasets)
    std_y = std(dataset_y, mean_y, size_datasets)

    covariance_value = covariance(dataset_x, dataset_y, mean_x, mean_y)
    pearson_correlation_coefficient_value = pearson_correlation_coefficient(covariance_value, std_x, std_y, size_datasets)
    print(round(pearson_correlation_coefficient_value, 3))
