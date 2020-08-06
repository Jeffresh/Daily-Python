# In the topic, you were given an algorithm that finds the first index of the maximum element in a list of numbers.
# Your task here is to modify that algorithm so that it finds the last index of the maximum element.
#
# The input and output examples below are there to give you the idea of the algorithm. You do NOT need to work with
# the input, call the function, or print anything!


def last_indexof_max(numbers):
    index = -1
    if numbers:
        min_value = -1
        for i, value in enumerate(numbers):
            if value >= min_value:
                min_value = value
                index = i

    return index


if __name__ == '__main__':
    print(last_indexof_max([1, 89, 89, 2, 8, 72]))
