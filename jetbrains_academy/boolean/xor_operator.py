# implement an XOR operator that can work with objects of any type.
#
# The behaviour should be the following:
#
#     if the operands are both truthy or both falsy, return False,
#     if one operand is truthy and the other operand is falsy, return the truthy one.
#
# Write your code inside the xor() function. Your program should not read any input or call the function,
# your task is to implement it.


def xor(a, b):
    return bool(a) != bool(b) and (a or b)


if __name__ == '__main__':
    a = input()
    b = input()
    print(xor(a, b))
