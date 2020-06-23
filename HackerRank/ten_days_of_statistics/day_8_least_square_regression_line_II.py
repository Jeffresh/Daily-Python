# Task
# A group of five students enrolls in Statistics immediately after taking a Math aptitude test.
# Each student's Math aptitude test score, x, and Statistics course grade, y,
# can be expressed as the following list of (x,y) points.
# Determine the equation of the best-fit line using the least squares method, then compute and print the value of y
# when x = 80.

# using sklearn

from sklearn import linear_model
import numpy as np

if __name__ == '__main__':
    x, y = [], []
    for _ in range(5):
        i = input().split()
        x.append(int(i[0]))
        y.append(int(i[1]))

    evalue = 80
    x = np.asarray(x).reshape(-1, 1)
    lm = linear_model.LinearRegression()
    lm.fit(x, y)
    print(lm.intercept_)
    print(lm.coef_[0])
    print(lm.predict(np.array([[80]])))
