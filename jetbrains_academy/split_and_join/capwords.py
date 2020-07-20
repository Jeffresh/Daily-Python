# In Python, the names of classes follow the CapWords convention. Let's convert the input phrase accordingly by capitalizing all words and spelling them without underscores in-between.
#
# The input format:
#
# A word or phrase, with words separated by underscores, like function and variable names in Python.
#
# You might want to change the case of letters since they are not necessarily lowercased.
#
# The output format:
#
# The name written in the CapWords fashion.

if __name__ == '__main__':
    capitalize_words = input().title().split('_')
    print(''.join(capitalize_words))