import numpy as np


def normal_equation(x, y):
    return np.linalg.inv(x.T @ x) @ x.T @ y


if __name__ == '__main__':
    n_features, n_data = map(int, input().split())
    x, y = [], []

    for _ in range(n_data):
        *features, y_val = map(float, input().split())
        x.append([1] + features)
        y.append(y_val)

    n_test = int(input())

    x_test = []
    for _ in range(n_test):
        x_test.append([1] + list(map(float, input().split())))

    y_train = np.array(y)
    x_train = np.array(x)

    theta = np.array(normal_equation(x_train, y_train))

    y_estimated = np.dot(x_test, theta)
    print("\n".join([str(i) for i in y_estimated.tolist()]))
