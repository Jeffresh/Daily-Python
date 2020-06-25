def merge_the_tools(string, k):
    subst = ''
    substrings = []
    for i in range(0, len(string)):
        if string[i] not in subst:
            subst = subst + string[i]
        if (i + 1) % k == 0:
            substrings.append(subst)
            subst = ''

    print('\n'.join(substrings))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
