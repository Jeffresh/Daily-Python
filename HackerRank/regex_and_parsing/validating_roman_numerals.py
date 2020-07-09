# You are given a string, and you have to validate whether it's a valid Roman numeral.
# If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.

import re

if __name__ == '__main__':
    thousand = 'M{0,3}'
    hundred = '(C[MD]|D?C{0,3})'
    ten = '(X[CL]|L?X{0,3})'
    digit = '(I[VX]|V?I{0,3})'

    regex_pattern = r''+thousand + hundred + ten + digit + '$'

    print(bool(re.match(regex_pattern, input())))
