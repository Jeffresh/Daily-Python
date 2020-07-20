# Find all words that end in "s" and print them together separated by an underscore.
#
# Sample Input 1:
#
# First ladies rule the State and state the rule: ladies first
#
# Sample Output 1:
#
# ladies_ladies

if __name__ == '__main__':
    word_list = input().split()
    s_words = [x for x in word_list if x.endswith('s')]
    print('_'.join(s_words))
