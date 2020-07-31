# The template for this function is defined below. Your task is to create additional functions
# (one for each case) and complete f(x). The additional functions are named f1(x), f2(x), and f3(x).
#
# You do NOT need to work with the input or print anything.

def f1(x):
    return x ** 2 + 1


def f2(x):
    return 1 / (x ** 2)


def f3(x):
    return x ** 2 - 1


def f(x):
    if x <= 0:
        return f1(x)
    if 0 < x < 1:
        return f2(x)

    return f3(x)


if __name__ == '__main__':
    print(f(0.3))
