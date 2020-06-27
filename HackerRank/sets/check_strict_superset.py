# task
# You are given a set A and other sets.
# Your job is to find whether set A is a strict superset of each of the N sets.
# Print True, if is a strict superset of each of the sets. Otherwise, print False.
# A strict superset has at least one element that does not exist in its subset.
#
# Input Format
#
# The first line contains the space separated elements of set A .
# The second line contains integer n , the number of other sets.
# The next n lines contains the space separated elements of the other sets.

if __name__ == '__main__':
    set_a = set(map(int, input().split()))
    n_sets = int(input())

    other_sets = set()
    for _ in range(n_sets):
        other_sets |= set(map(int, input().split()))

    print(set_a == other_sets)
