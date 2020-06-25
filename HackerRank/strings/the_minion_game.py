def minion_game(string):
    stuart, kevin, ln = 0, 0, len(string)
    vowels = 'AEIOU'

    for i in range(ln):
        if string[i] in vowels:
            kevin += ln - i
        else:
            stuart += ln - i

    if stuart > kevin:
        print('Stuart', stuart)
    elif stuart == kevin:
        print('Draw')
    else:
        print('Kevin', kevin)


if __name__ == '__main__':
    s = input()
    minion_game(s)