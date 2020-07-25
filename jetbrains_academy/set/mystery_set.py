# There is an unknown set of objects named mystery_set which has been defined beforehand.
# You don't have access to this set.
#
# Write a program that deletes the input string (stored in the variable string) from the mystery_set.
# It is NOT guaranteed that the string is an element of the mystery_set to begin with. Don't forget to take that
# into account!
#
# Don't print anything!

if __name__ == '__main__':
    # mystery_set has been defined
    string = input()

    # delete string from mystery_set
    mystery_set.discard(string)
