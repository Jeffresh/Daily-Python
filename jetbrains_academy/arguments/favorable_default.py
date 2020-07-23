# Write a short function code that will print out this message:
#
# We code in {language}
#
# Set "Python" as a default value to the language parameter.
#
# You don't need to call the function, you only need to implement it.


def code(language='Python'):
    print('We code in {}'.format(language))


if __name__ == '__main__':
    code(input('Write your favourite coding language'))
