# Python is widely used for mathematical purposes. Let's start gaining experience by using the
# betavariate(alpha, beta) function from the random module.
#
# Generate a number from the beta distribution with parameters alpha=0.9 and beta=0.1. Print your result.
#

import random

if __name__ == '__main__':
    random.seed(3)
    alpha, beta = 0.9, 0.1
    print(random.betavariate(alpha, beta))