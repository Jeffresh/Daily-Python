# Task
# Given 2 sets of integers, M and N , print their symmetric difference in ascending order.
# The term symmetric difference indicates those values that exist in either M or N but do not exist in both.


if __name__ == '__main__':
    n_set_a = int(input())
    set_a = set(map(int, input().split()))
    n_set_b = int(input())
    set_b = set(map(int, input().split()))

    only_a = set_a.difference(set_b)
    only_b = set_b.difference(set_a)
    only_a.update(only_b)

    print(*sorted(only_a, key=int), sep='\n')
