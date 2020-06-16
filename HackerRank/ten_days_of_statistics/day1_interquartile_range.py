# Task
# The interquartile range of an array is the difference between its first () and third () quartiles (i.e.,
#
# ).
#
# Given an array,
# , of integers and an array, , representing the respective frequencies of 's elements, construct a data set, , where each occurs at frequency . Then calculate and print 's interquartile range, rounded to a scale of decimal place (i.e.,
#
# format).
#
# Tip: Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to not include the median in your upper and lower data sets.
#

def quartiles(l):
    l.sort()
    size = len(l)

    middle_point = int(size / 2)

    if size % 2 == 0:
        q2 = (l[middle_point - 1] + l[middle_point]) / 2
        lower_half = l[0:middle_point]
        upper_half = l[middle_point:]
    else:
        q2 = l[middle_point]
        lower_half = l[0:middle_point]
        upper_half = l[middle_point + 1:]

    lower_half_size = int(len(lower_half) / 2)
    upper_half_size = int(len(upper_half) / 2)

    if len(lower_half) % 2 == 0:
        q1 = (lower_half[lower_half_size - 1] + lower_half[lower_half_size]) / 2
        q3 = (upper_half[upper_half_size - 1] + upper_half[upper_half_size]) / 2

    else:
        q1 = lower_half[lower_half_size]
        q3 = upper_half[upper_half_size]

    return q1, q2, q3


if __name__ == '__main__':
    data = [10, 40, 30, 50, 20, 10, 40, 30, 50, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 10, 40, 30, 50, 20, 10, 40, 30,
            50]
    frequencies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 40, 30, 50, 20, 10, 40, 30, 50, 20]
    dataset = []
    for element, frec in zip(data, frequencies):
        dataset = dataset + [element] * frec

    q1, q2, q3 = quartiles(dataset)

    print('{0:.1f}'.format(q3 - q1))
