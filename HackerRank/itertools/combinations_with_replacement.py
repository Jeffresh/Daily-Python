# Task
#
# You are given a string S.
# Your task is to print all possible size K replacement combinations of the string in lexicographic sorted order.
from itertools import combinations_with_replacement

if __name__ == '__main__':
    word, group = input().split()
    group = int(group)
    word = list(word)
    word.sort()

    print(*[''.join(i) for i in combinations_with_replacement(word, group)], sep='\n')
