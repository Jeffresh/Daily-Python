def factorial(n):
    fact = 1
    while n != 0:
        fact *= n
        n = n - 1
    return fact


if __name__ == '__main__':
    print(factorial(int(input())))
