# Task
# You are given an integer, N . Your task is to print an alphabet rangoli of size N .
# (Rangoli is a form of Indian folk art based on creation of patterns.)


import string


def print_rangoli(n):
    alpha = string.ascii_lowercase
    elements = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        elements.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))

    rangoli = '\n'.join(elements[:0:-1] + elements)
    print(rangoli)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
