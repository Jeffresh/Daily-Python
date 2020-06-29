# Task
#
# You are given a two lists A and B
# Your task is to compute their cartesian product AXB.
from itertools import product

if __name__ == '__main__':
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))

    print(*product(list_a, list_b))
