# Convert a text into lowerCamelCase, or mixedCase.
#
# The input format:
#
# A lowercased word or several words separated by spaces.
#
# The output format:
#
# Print this text stylized as mixedCase, that is, the first word should be in lowercase and all other words – capitalized.

if __name__ == '__main__':
    word_list = input().split()
    if len(word_list) > 1:
        word_list = [word_list[0]] + [x.capitalize() for x in word_list[1:]]
    print(''.join(word_list))
