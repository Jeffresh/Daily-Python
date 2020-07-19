# Given a numeric sequence, create a list in which each number will be a digit from this
# input string. Then use this list to calculate the running total, or cumulative sum.
# Essentially, it's a new list of partial sums that gets updated every time a new element appears.
#
# For example, we can transform the list [1, 2, 3] to [1, 1 + 2, 1 + 2 + 3],
# which equals to [1, 3, 6].

if __name__ == '__main__':
    digits = list(map(int, input()))
    print([sum(digits[:i + 1]) for i in range(len(digits))])

