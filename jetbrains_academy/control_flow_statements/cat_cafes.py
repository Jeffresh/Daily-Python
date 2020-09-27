# Kitty wants to visit a cat café! Help her find the one with the largest number of cats.
#
# Input format
#
# Each string contains a café's name followed by a space and the number of cats in it, e.g. Paws 11, Kittens 9.
#
# The names would be one-word only. Read input lines until you get a string MEOW (without any number).
#
# Output format
#
# The café with the maximum number of cats.


if __name__ == '__main__':
    name_cat, number_cat = input().split()
    number_cat = int(number_cat)
    max_cats = 0
    max_name = name_cat
    while name_cat != "MEOW":
        if max_cats < number_cat:
            max_cats = number_cat
            max_name = name_cat
        name_cat = input()
        name_cat, number_cat = name_cat.split()[0], int(name_cat.split()[1]) \
            if len(name_cat.split()) > 1 else [name_cat.split(), 0]

    print(max_name)
