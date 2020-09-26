# let's do some text formatting. Read an input word and print it with an indicated number of spaces between
# the letters. There are two different inputs: a word in the first line and a number of spaces in the second line

# Sample Input 1:
#
# earnest
# 1
#
# Sample Output 1:
#
# e a r n e s t
#
#  Sample Input 2:
#
# Ernest
# 2
#
# Sample Output 2:
#
# E  r  n  e  s  t

if __name__ == '__main__':
    name = input()
    sep_spaces = int(input())
    print(*name, sep=' ' * sep_spaces)
