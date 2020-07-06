# Task
#
# You are given a space separated list of integers.
# If all the integers are positive, then you need to check if any integer is a palindromic integer.

if __name__ == '__main__':
    n_lines = int(input())
    number_list = input().split()
    print(all(['-' not in x for x in number_list]) and any([x == x[::-1] for x in number_list]))
