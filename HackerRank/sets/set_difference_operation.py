# Task
#
# Students of District College have a subscription to English and French newspapers.
# Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper,
# and some have subscribed to both newspapers.
#
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper,
# and one set has subscribed to the French newspaper.
# Your task is to find the total number of students who have subscribed to only English newspapers.

if __name__ == '__main__':
    a_size = int(input())
    set_a = set(map(int, input().split()))
    b_size = int(input())
    set_b = set(map(int, input().split()))

    print(len(set_a.difference(set_b) | set_b.difference(set_a)))
