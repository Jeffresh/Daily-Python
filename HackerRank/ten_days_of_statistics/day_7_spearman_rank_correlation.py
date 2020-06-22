# Task
# Given two n -element data sets, X and Y calculate the value of Spearman's rank correlation coefficient.
#
# Input Format
#
# The first line contains an integer, n , denoting the number of values in data sets X and Y .
# The second line contains n space-separated real numbers (scaled to at most one decimal place) denoting data set X.
# The third line contains n space-separated real numbers (scaled to at most one decimal place) denoting data set Y .

# rs (spearman rank correlation coefficient) is equal to Pearson correlation coefficient of Rankx and Ranky.
# rank is equal of the order on the list.
# Special case if X and Y dont contain duplicates then rs = 1- (6 * sum(rankxi - rankxj))/(n*n^2 -1)

def rank(data):
    rx = [sorted(x).index(x) for x in data]
    return rx

