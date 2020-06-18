# Task
# Suppose a family has children, one of which is a boy.
# What is the probability that both children are boys?

if __name__ == '__main__':
    space = ['bb', 'bg', 'gb', 'gg']
    p_b = len([True for x in space if 'b' in x]) / len(space)
    p_b_bb = 1
    p_bb = 1/4

    p_bb_b = (p_b_bb * p_bb)/p_b
    print(p_bb_b)
