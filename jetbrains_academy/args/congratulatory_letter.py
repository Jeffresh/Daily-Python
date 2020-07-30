# Imagine that you were instructed to write a congratulatory letter, mentioning all the employees of the IT
# department in it. You know for sure that the department has one tester, one project manager, but you don't
# know exactly how many developers are there.
#
# Define a function congratulations() that lists the names of everyone in the letter.
# If the project manager is Alice, the tester is Mike, and the developers are Roman and Victoria, then the printed
# congratulation should look like this:
#
# Happy New Year! Take care of yourself and your loved ones!
# For:
# Alice
# Mike
# Roman
# Victoria
#
# Pay attention to the order of names. First mention a project manager, then a tester, and then developers.
# Each name should be on a separate line!
#
# Note that you do not need to call a function, just implement it.
#
# Sample Input 1:
#
# Alice
# Mike
# Roman Victoria
#
# Sample Output 1:
#
# Happy New Year! Take care of yourself and your loved ones!
# For:
# Alice
# Mike
# Roman
# Victoria


def congratulations(*args):
    print('Happy New Year! Take care of yourself and your loved ones! \nFor:')
    print(*args, sep='\n')


if __name__ == '__main__':
    congratulations("Alice", "Mike", "Roman", "Victoria")
