# Task
# You are given a string S
# Your task is to print all possible combinations, up to size K , of the string in lexicographic sorted order.
from itertools import combinations

if __name__ == '__main__':
    word, group = input().split()
    group = int(group)
    word = list(word)
    word.sort()

    print(*[''.join(i) for k in range(1, group + 1) for i in combinations(word, k)], sep='\n')
