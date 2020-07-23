# Markdown syntax is used to format a text. To create a heading, you should add # in front of a word or phrase.
# The number of hash signs # corresponds to the heading level, ranging from 1 to 6:
#
# # Heading level 1
# ## Heading level 2
# ### Heading level 3
# #### Heading level 4
# ##### Heading level 5
# ###### Heading level 6
#
# Define a function heading() that turns a string into a markdown heading. By default, it will be a
# first-level heading, but there should be a chance to change it to the desired value. However, if the specified level
# is less than 1, return a first-level heading. Similarly, if the level is greater than 6, think of it as a sixth-level
# heading. Look at these examples:
#
# heading("A")      # Returns "# A"
# heading("A", 3)   # Returns "### A"
# heading("A", 1)   # Returns "# A"
# heading("A", 0)   # Returns "# A"
# heading("A", 10)  # Returns "###### A"
#
# Don't call your function, just implement it!
#
# NB: you function should return the result, not print it.


def heading(message, level=1):
    if level < 1:
        level = 1
    elif level > 6:
        level = 6
    return '#' * level + ' ' + message


if __name__ == '__main__':
    print(heading('A', 3))
