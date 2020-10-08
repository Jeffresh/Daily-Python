# Palindrome is a word or a text that reads the same backward as forward. Create a program that checks
# if the word is palindrome.
#
# The input format:
#
# Word that needs to be checked. It is guaranteed that the word will be of even length.
#
# The output format:
#
# If the word is palindrome, write Palindrome. Otherwise, write Not palindrome


if __name__ == '__main__':
    word = input()
    if (lambda x: x == x[::-1])(word):
        print('Palindrome')
    else:
        print('Not Palindrome')
