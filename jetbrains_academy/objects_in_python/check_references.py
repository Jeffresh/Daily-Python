# Imagine, you have two variables and you don't know what they contain but need to check if
# they refer to the same object or not. How would you do that?
#
# Write a function check(obj1, obj2) that will take two objects and print True if they refer to
# the same object and False otherwise.


def check(obj1, obj2):
    print(id(obj1) == id(obj2))


if __name__ == '__main__':
    a = list()
    b = a
    check(a, b)
