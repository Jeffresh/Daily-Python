# Task
#
# You are given a string S.
# Your task is to find out if the string contains:
# alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.


def string_validators(string):
    n = len(string)
    i = 0
    prints = [False] * 5
    trues = 0

    while i != n and trues < 5:
        if not prints[0]:
            if string[i].isalnum():
                prints[0] = True
                trues = trues + 1
        if not prints[1]:
            if string[i].isalpha():
                prints[1] = True
                trues = trues + 1
        if not prints[2]:
            if string[i].isdigit():
                prints[2] = True
                trues = trues + 1
        if not prints[3]:
            if string[i].islower():
                prints[3] = True
                trues = trues + 1
        if not prints[4]:
            if string[i].isupper():
                prints[4] = True
                trues = trues + 1
        i = i + 1

    for boolean in prints:
        print(boolean)


def string_validator_discussion(string):
    for f in ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']:
        print(any(getattr(c, f)() for c in string))


if __name__ == '__main__':
    string = input()
    string_validator_discussion(string)
