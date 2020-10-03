# Let's work with texts! You'll get a sequence of characters (a word, a sentence or just gibberish). For each
# character tell if it's a vowel or a consonant. If you hit a non-alphabetic symbol, just stop processing.
#
# The input format:
#
# One line with N characters.
#
# We will use letters from the English alphabet. The symbols "aeiou" are considered vowels. Treat the rest of the
# letters as consonants.
#
# The output format:
#
# Print "vowel" if the character is a vowel, and "consonant" if the character is consonant. Stop printing information
# at the first non-alphabetic symbol.

if __name__ == '__main__':
    vowel = 'aeiou'
    index = 0
    word = input()
    word_size = len(word)

    while index < word_size and word[index].isalpha():
        if word[index] in vowel:
            print('vowel')
        else:
            print('consonant')
        index += 1
