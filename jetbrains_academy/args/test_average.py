# Imagine that you are a teacher whose students recently wrote a test. However, you do not know exactly how
# many students were in the class at the time of writing. Based on the marks you have, you should calculate the
# average mark for this test.
#
# Define the average_mark() function that takes a varying number of marks and returns the average value.
#
# Round the result to one decimal place.
#
# You are not supposed to call the function, just implement it.


def average_mark(*args):
    return round(sum(args) / len(args), 1)


if __name__ == '__main__':
    print(average_mark(3, 5, 8, 9, 3, 6, 8, 3))
