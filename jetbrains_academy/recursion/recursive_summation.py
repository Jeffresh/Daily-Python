# Write a recursive function rec_sum() that takes some natural number n as its input and outputs the sum of
# first n natural numbers.
#
# This problem is very similar to that of finding a factorial, so we are sure that you'll be able
# to get it right!


def rec_sum(n):
    if n == 0:
        return 0
    return n + rec_sum(n - 1)


if __name__ == '__main__':
    print(rec_sum(3))
