# Task
# In a single toss of 2 fair (evenly-weighted) six-sided dice,
# find the probability that the values rolled by each die will be different and the two dice have a sum of 6.

import itertools

if __name__ == '__main__':
    dice = [1, 2, 3, 4, 5, 6]
    two_toss = dice * 2
    natural_product = set(list(itertools.combinations(two_toss, 2)))
    sum_nine = [x for x in natural_product if sum(x) == 6 and x[0] != x[1]]
    favorable_outcomes = len(sum_nine)
    total_outcomes = len(natural_product)
    print(sum_nine)
    print(favorable_outcomes)
    print(total_outcomes)
    print(natural_product)
