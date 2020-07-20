# Write a spellchecker that tells you which words in the sentence are spelled incorrectly.
# Use the dictionary in the code below.
#
# The input format:
#
# A sentence. All words are in the lowercase.
#
# The output format:
#
# All incorrectly spelled words in the order of their appearance in the sentence.
# If all words are spelled correctly, print OK.

if __name__ == '__main__':
    dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
                  'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
                  'sign', 'the', 'to', 'uncertain']

    word_list = input().split()

    incorrect_words = [x for x in word_list if x not in dictionary]
    print(*incorrect_words, sep='\n') if incorrect_words else print('OK')
