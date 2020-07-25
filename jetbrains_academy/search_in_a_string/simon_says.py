# Do you know the game "Simon says"? The instructor, "Simon", says what the players should do, e.g.
# "jump in the air" or "close your eyes". The players should follow the instructions only if the phrase
# starts with "Simon says". Now, let's implement a digital version of this game! We will modify it a bit:
# the correct instructions may not only start but also end with the words "Simon says".
#
# Write a function that takes a string with instructions: if it starts or ends with the words "Simon says",
# your function should return the string "I " plus what you would do: the instructions themselves. Otherwise,
# return "I won't do it!".
#
# You are not supposed to handle input or call your function, just implement it.
#
# To get a substring of a string from its beginning till a specific index, use string[:ind+1]. In this case,
# the element with the index ind will be included. The other way round, to get a substring from a specific
# index till the end of the string, use string[ind:].
#
#


def what_to_do(instructions):
    ind = instructions.find('Simon says')

    if ind != -1:
        if instructions.startswith("Simon says"):
            return 'I ' + instructions[ind + 11:]
        if instructions.endswith("Simon says"):
            return 'I ' + instructions[:ind]

    return "I won't do it!"


if __name__ == '__main__':
    print(what_to_do("Simon says fuck you"))
