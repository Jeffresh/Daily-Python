# Everybody wants to speak like master Yoda sometimes. Let's try to implement a program that will help us with it.
#
# First, we turn the string of words into a list using the string.split() method.
#
# Then use the function random.seed(43) and rearrange the obtained sequence.
#
# To turn the list back into a string, use ' '.join(list).
#
# Print the message in the end.

import random

if __name__ == '__main__':
    random.seed(43)
    message = input().split()
    random.shuffle(message)

    print(' '.join(message))
