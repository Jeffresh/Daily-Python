# Create a list of words from the text below that are shorter
# than or equal to the input value. Print the new list.
#
# Sample Input 1:
#
# 1
#
# Sample Output 1:
#
# ['a', 'a']

if __name__ == '__main__':
    text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary",
             "setback"],
            ["Ephemeral", "lasts", "one", "day", "only"],
            ["Accolade", "is", "an", "expression", "of", "praise"]]

    n = int(input())

    print([word for lists in text for word in lists if len(word) <= n])
