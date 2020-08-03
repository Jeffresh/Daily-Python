# Your task is to write a function print_book_info(title, author=None, year=None) that prints information about
# a book. Arguments author and year are optional, so be ready that they might equal to None.
#
# You don't have to read the input. The information about a book will be passed to your function, and it
# should output it in the right format.
#
# See the samples below to understand the output format.


def print_book_info(title, author=None, year=None):
    info = '"{}"'.format(title)
    if author or year:
        info += ' was written'
        if author:
            info += ' by {}'.format(author)
        if year:
            info += ' in {}'.format(year)
    print(info)


if __name__ == '__main__':
    print_book_info('The lord of the rings', 'J.R.R Tolkien')