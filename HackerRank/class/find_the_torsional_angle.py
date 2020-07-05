# You are given four points, A,B,C and D in a 3-dimensional Cartesian coordinate system. Y
# ou are required to print the angle between the plane made byt the points, A,B,C and B,C,D in degrees(not radinas).
# Let the angle be PHI. Cos(PHI) = (X.Y)/|X||Y| where X = AB x BC and Y = BC x CD.
# Here, X.Y means the dot product of X and Y, and AB xBC means the cross product of vectors AB and BC. Also, AB = B - A

# Input Format
# One line of input contain the space separated floating number values of the X,Y and Z coordinates of a point.
# Output Format
# Output the angle correct up to two decimal places.

import math


class Points(object):
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __sub__(self, no):
        return Points(no.x - self.x, no.y - self.y, no.z - self.z)

    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        x_part = self.y * no.z - self.z * no.y
        y_part = self.z * no.x - self.x * no.z
        z_part = self.x * no.y - self.y * no.x
        return Points(x_part, y_part, z_part)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
