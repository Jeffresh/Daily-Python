# Declare a function sq_sum() that calculates the squares for arguments passed into it and returns their sum.
#
# print(sq_sum(1, 2, 2, 4))  # 25.0
# print(sq_sum(1.5))         # 2.25
# print(sq_sum(1, 10, 10))   # 201.0
#
# Your function is not supposed to print anything, just return the calculated sum


def sq_sum(*args):
    return sum([x ** 2 for x in args])


if __name__ == '__main__':
    print(sq_sum(2, 2, 2))
