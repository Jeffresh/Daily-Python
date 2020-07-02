# Task
#
# Perform append, pop, popleft and appendleft methods on an empty deque d.

from collections import deque

if __name__ == '__main__':
    itn_number = int(input())
    d = deque()
    for _ in range(itn_number):
        ins = input().split()
        getattr(d, ins[0])(*ins[1] if len(ins) > 1 else [])

    print(*d)
