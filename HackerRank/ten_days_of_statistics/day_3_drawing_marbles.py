# Task
# A bag contains red marbles and blue marbles. Then, marbles are drawn from the bag, at random, without replacement.
# If the first marble drawn is red, what is the probability that the second marble is blue?

import itertools

if __name__ == '__main__':
    marbles_bag = [0, 0, 0, 1, 1, 1, 1]

    states = list(itertools.permutations(marbles_bag, 2))
    red_and_blue = [x for x in states if x[0] == 0 and x[1] == 1]
    red = [x for x in states if x[0] == 0]

    n_outcomes = len(states)
    p_rb = len(red_and_blue) / n_outcomes
    p_b = len(red) / n_outcomes

    p_rb_b = p_rb / p_b

    print(p_rb_b)
