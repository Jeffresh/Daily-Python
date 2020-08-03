# Write a function that returns an object whose identity ends with 888.
#
# Iterate numbers from 0 to 10 000 and check their identity via id() to find a value ending with ...888.
#


def object_with_beautiful_identity():
    end888 = None
    for i in range(10_000):
        # Change the next line
        if str(id(i)).endswith('888'):
            end888 = i
    return end888


if __name__ == '__main__':
    object_with_beautiful_identity()
