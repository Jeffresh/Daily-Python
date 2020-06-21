# Task
# You have a sample of 100 values from a population with mean 500 and with standard deviation 80 .
# Compute the interval that covers the middle 95% of the distribution of the sample mean; in other words,
# compute A and B such that P(A < x < B) = 0.95. Use the value of z = 1.96


from math import sqrt

if __name__ == '__main__':
    n = int(input())
    mean = int(input())
    std = int(input())
    interval = float(input())
    z = float(input())

    # using z value

    # mean of sample mean  = mean, deviation of sample mean  =  deviation / sqrt(n)

    sqrt_n = sqrt(n)

    sample_mean = mean
    sample_deviation = std / sqrt_n

    # prediction invervals using z value (standard score) of a distribution of the sample mean

    pl = sample_mean - sample_deviation * z
    pr = sample_mean + sample_deviation * z

    print('{0:.2f}'.format(pl))
    print('{0:.2f}'.format(pr))
