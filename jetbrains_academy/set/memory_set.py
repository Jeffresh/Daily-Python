# Today you are assisting in a psychological experiment. To test a short-term memory,
# a researcher gives a set of numbers to each volunteer and asks to repeat all of them in any order.
# Repeats are allowed in the answer, but not the numbers not mentioned earlier.
#
# The input has been read into two variables for you.
#
# If the volunteer remembers the numbers correctly, print True, otherwise, you should output False.

if __name__ == '__main__':
    numbers = input().split()
    answers = input().split()

    print(set(numbers) == set(answers))
