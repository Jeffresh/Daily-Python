# Write a concat() function that will take an arbitrary number of strings and combine
# them into one through a separator (the keyword argument sep). If no separator is specified,
# then it should separate the strings by spaces:
#
# print(concat("turtle"))                # "turtle"
# print(concat("cat", "dog"))            # "cat dog"
# print(concat("a", "b", "c", sep=":"))  # "a:b:c"
#
# You do not need to call a function, just implement it.


def concat(*args, sep=' '):
    return sep.join(args)


if __name__ == '__main__':
    print(concat("turtle"))  # "turtle"
    print(concat("cat", "dog"))  # "cat dog"
    print(concat("a", "b", "c", sep=":"))  # "a:b:c"
