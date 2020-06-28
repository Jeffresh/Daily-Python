# Therefore ABC = 90
# M is the midpoint of hypotenuse AC
#
# You are given the lengths AB and BC
# Your task is to find  MBC (angle Theta , as shown in the figure) in degrees.

from math import sqrt, acos, degrees

if __name__ == '__main__':
    ab = int(input())
    bc = int(input())

    ac = sqrt(ab ** 2 + bc ** 2)
    m = ac / 2

    an = acos(bc / ac)
    de = degrees(an)
    print(round(de), chr(176), sep='')

