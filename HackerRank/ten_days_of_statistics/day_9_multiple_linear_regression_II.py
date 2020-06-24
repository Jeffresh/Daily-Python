# using sklearn

from sklearn import linear_model
import numpy as np

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
    lm = linear_model.LinearRegression()
    lm.fit(x_train, y_train)
    a = lm.intercept_
    b = lm.coef_
    print(lm.predict(x_test))
