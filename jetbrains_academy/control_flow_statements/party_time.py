# James is hosting a party today. He decided to welcome all new guests personally. To remember their,
# James kindly asks you to write them in a list. Read the names from the input, each on a new line, and stop
# at a single period . that denotes the end of the sequence.
#
# Print your list and its length (the number of guests) for James.


# Sample Input 1:
#
# Katja
# Adam
# Eva
# Nicholas
# .
#
# Sample Output 1:
#
# ['Katja', 'Adam', 'Eva', 'Nicholas']
# 4


if __name__ == '__main__':
    name = input()
    names_lists = []

    while name != '.':
        names_lists.append(name)
        name = input()
    else:
        print(names_lists, len(names_lists), sep='\n')
