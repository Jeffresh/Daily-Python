# Task
# Given an array, , of integers, calculate the
# respective first quartile (), second quartile (), and third quartile (). It is guaranteed that , , and are integers.

def quartiles(data):
    data.sort()
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
        q1 = (lower_half[lower_half_size - 1] + lower_half[lower_half_size]) // 2
        q3 = (upper_half[upper_half_size - 1] + upper_half[upper_half_size]) // 2

    else:
        q1 = lower_half[lower_half_size]
        q3 = upper_half[upper_half_size]

    return q1, q2, q3


if __name__ == '__main__':
    l = [3, 7, 8, 5, 12, 14, 21, 15, 18, 14]
    l1 = [4, 17, 7, 14, 18, 12, 3, 16, 10, 4, 4, 12]

    q1, q2, q3 = quartiles(l)

    print(int(q1))
    print(int(q2))
    print(int(q3))
