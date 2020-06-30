# Task
# You are given a list N of lowercase English letters. For a given integer K , you can select any K indices (assume
#
# 1-based indexing) with a uniform probability from the list.
#
# Find the probability that at least one of the K indices selected will contain the letter: 'a'.
from itertools import combinations

if __name__ == '__main__':
    size = int(input())
    letters = input().split()
    n_index = int(input())
    C = list(combinations(letters, n_index))
    size_C = len(C)
    a_num = sum([1 for x in C if 'a' in x])
    print(a_num / size_C)
