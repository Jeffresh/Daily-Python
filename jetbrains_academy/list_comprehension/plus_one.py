# You are given a list of strings containing integer numbers.
# Print the list of their values increased by 1.
#
# E.g. if list_of_strings = ["36", "45", "99"], your program should print the list [37, 46, 100].
#
# The variable list_of_strings is already defined, you don't need to work with the input.

if __name__ == '__main__':
    list_of_strings = ["36", "45", "99"]
    print([int(x) + 1 for x in list_of_strings])
