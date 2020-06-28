# Task
# You are given a complex z .
# Your task is to convert it to polar coordinates.

import cmath

if __name__ == '__main__':
    n = input()
    mod = abs(complex(n))
    angle = cmath.phase(complex(n))
    print(mod)
    print(angle)
