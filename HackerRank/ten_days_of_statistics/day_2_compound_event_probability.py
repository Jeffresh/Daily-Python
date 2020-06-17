#
# Task
# There are
# urns labeled X, Y and Z

# Urn  X contains 4 red balls and 3 black balls.
# Urn Y contains 5 red balls and 4 black balls.
# Urn Z contains 4 red balls and 4 black balls.
#
# One ball is drawn from each of the
# urns. What is the probability that, of the balls drawn, are red and is black?
import itertools

if __name__ == '__main__':
    X = [1, 1, 1, 1, 2, 2, 2]
    Y = [1, 1, 1, 1, 1, 2, 2, 2, 2]
    Z = [1, 1, 1, 1, 2, 2, 2, 2]
    space = [1, 2] * 3
    natural_product = set(list(itertools.combinations(space, 3)))
    print(natural_product)

    favorable_outcomes = [x for x in natural_product if x.count(1) == 2 and x.count(2) == 1]
    print(favorable_outcomes)

    x_total_outcomes = len(X)
    y_total_outcomes = len(Y)
    z_total_outcomes = len(Z)

    prb_x = [X.count(1)/x_total_outcomes, X.count(2)/x_total_outcomes]
    prb_y = [Y.count(1)/y_total_outcomes, Y.count(2)/y_total_outcomes]
    prb_z = [Z.count(1)/z_total_outcomes, Z.count(2)/z_total_outcomes]

    print(prb_x)
    print(prb_y)
    print(prb_z)

    p_two_red_and_1_black = sum([prb_x[x[0]-1] * prb_x[x[1]-1] * prb_z[x[2]-1] for x in favorable_outcomes])
    print(p_two_red_and_1_black)




