# Write a program that takes a list of numbers, creates another list of even numbers
# from the first list, and prints it.
#
# E.g. if my_numbers = [1, 2, 3, 4, 5], then your program should print the list [2, 4].
#
# NB: the list with numbers my_numbers is already defined, so you don't have
# to work with the input.

if __name__ == '__main__':
    my_numbers = [1, 2, 3, 4, 5]

    print([x for x in my_numbers if x % 2 == 0])
