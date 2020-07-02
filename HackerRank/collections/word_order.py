# Task
# You are given words. Some words may repeat. For each word, output its number of occurrences.
# The output order should correspond with the input order of appearance of the word.

from collections import OrderedDict

if __name__ == '__main__':
    word_number = int(input())

    words = OrderedDict()
    for _ in range(word_number):
        key = input()
        words[key] = words.get(key, 0) + 1

    print(len(words))
    print(*words.values(), sep=' ')
