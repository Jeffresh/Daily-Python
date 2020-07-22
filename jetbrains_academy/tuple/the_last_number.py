# Given a tuple consisting of numbers, print its last element.

if __name__ == '__main__':
    # use this tuple
    numbers = tuple(int(n) for n in input().split())
    print(numbers[-1])
