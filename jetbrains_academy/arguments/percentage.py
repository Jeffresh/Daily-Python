# Write a function get_percentage that takes a real number and represents it as a percentage. So, for example,
# 0.1 will be equal to 10%, while 1.052 will be 105.2%. Also, add an optional parameter round_digits,
# which indicates a precision (the number of digits after the point). If it is not specified, round the result to the nearest integer.
# Here are some examples:
#
# print(get_percentage(0.0123))      # 1%
# print(get_percentage(0.0123, 0))   # 1.0%
# print(get_percentage(0.0123, 1))   # 1.2%
# print(get_percentage(0.0123, 10))  # 1.23%
#
# Don't forget to add the percent sign % after the number. The returned percentage should be a string.
#
# Just implement your function, you don't have to handle input or call it in your code.


def get_percentage(percentage, round_digits=None):
    return f'{round(percentage * 100, round_digits)}%'


if __name__ == '__main__':
    get_percentage(0.142)
