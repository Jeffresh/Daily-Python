# Task
# In this challenge, you will be given 2 integers, n and m . There are words, which might repeat, in word group A .
# There are m words belonging to word group B . For each m words, check whether the word has appeared in group A or not.
# Print the indices of each occurrence of m in group A. If it does not appear, print - 1 .
from collections import defaultdict

if __name__ == '__main__':

    n, m = map(int, input().split())
    d = defaultdict(list)
    for i in range(n):
        d[input()].append(i + 1)

    for i in range(m):
        print(' '.join(map(str, d[input()])) or -1)
