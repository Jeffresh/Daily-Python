# Task
# Mr. Vincent works in a door mat manufacturing company.
# One day, he designed a new door mat with the following specifications:
# Mat size must be N X M ( N is a odd natural number, and M is 3 times N)
# The design should have 'WELCOME' written in the center
# The design patter should only use |, . and - characters

if __name__ == '__main__':
    N, M = map(int, input().split())
    upper = [('.|.' * (2 * i + 1)).center(M, '-') for i in range(N//2)]
    center = ['WELCOME'.center(M, '-')]
    lower = upper[::-1]

    print('\n'.join(upper + center + lower))
