# There is a function called add_book() that takes a non-empty string containing the title of a book to add it to
# recommendations. Share your favorite book with us by calling this function. You don't have to declare it,
# just call it in your code.
#
# Importantly, specify the keyword argument title in the call. Otherwise, you may get an error.
def add_book(title):
    print('Your favorite film is {}'.format(title))


if __name__ == '__main__':
    add_book(title='The Goodfellas')
