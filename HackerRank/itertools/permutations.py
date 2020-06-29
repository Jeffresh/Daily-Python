# Task
# You are given a string S.
# Your task is to print all possible permutations of size K of the string in lexicographic sorted order.


from itertools import permutations

if __name__ == '__main__':
    word, group = input().split()
    group = int(group)
    word = list(word)
    word.sort()

    print(*[''.join(i) for i in permutations(word, group)], sep='\n')




