# To find out if a word is a palindrome we ould need to check if it reads the s ame forward and backward.
#
# The condition for that check has already been written in the code below, but the parts that need to be compared
# haven't been defined yet. Fiish the coe by defining variables forward and backward.
#
# The variable that stores the word in question is called word

if __name__ == '__main__':
    # please work with the preset variable `word`
    forward = word
    backward = word[::-1]

    if forward == backward:
        print("Yes")
    else:
        print("No")
