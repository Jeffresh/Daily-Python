# Let's say you've created a registration form for people wanting to take part in your online book club.
# In order to send them invitations, you need to know their email address, so you are writing a program to
# check whether the field "email" is filled correctly.
#
# Write a function that takes a string and checks that:
#
#     it doesn't contain spaces,
#     it contains the @ symbol,
#     after @, there's a dot.
#
# Note that dots may also occur before @, and in a correct address a dot shouldn't stand immediately after @.
#
# The function should return True if all of the conditions are true, and False otherwise.
#
# You are not supposed to handle input or call your function, just implement it.


def check_email(string):
    if ' ' not in string:
        ind_ar = string.find('@')
        return ind_ar != -1 and ind_ar + 1 < string.rfind('.')
    return False


if __name__ == '__main__':
    print(check_email('good.email@example.com'))
