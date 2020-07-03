# task
# Given a string , which is the company name in lowercase letters,
# your task is to find the top three most common characters in the string.


from collections import Counter

if __name__ == '__main__':
    word = sorted(list(input()))
    letter_counter = Counter(word).most_common(3)
    [print(*x) for x in letter_counter]
