# Write a program that takes a list with words, creates a new list of words that start
# with the letter "a" in the first list, and prints it.
#
# Some words may begin with the capital A! Leave them in their original
# form in the resulting list.
#
# E.g. if words = ['apple', 'pear', 'banana', 'Ananas'], then your
# program should print the list ['apple', 'Ananas'].
#
# The list with words is already defined: you can access it using the variable words.

if __name__ == '__main__':
    words = ['apple', 'pear', 'banana', 'Ananas']

    print([x for x in words if x.lower().startswith('a')])
