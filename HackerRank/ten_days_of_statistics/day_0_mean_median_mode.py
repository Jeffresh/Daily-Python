# Task
# Given an array, , of integers, calculate and print the respective mean, median,
# and mode on separate lines. If your array contains more than one modal value, choose the numerically smallest one.

if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))

    mean = sum(data) / n
    print('{0:.1f}'.format(mean))
    data_sorted = data.copy()
    data_sorted.sort()
    data_size = len(data_sorted)
    j = int(data_size / 2)
    if data_size % 2 == 0:
        i = int(data_size / 2) - 1
        median = (data_sorted[i] + data_sorted[j]) / 2
    else:
        median = data_sorted[j]
    print('{0:.1f}'.format(median))

    count_elements = [data_sorted.count(x) for x in data_sorted]
    index_max = count_elements.index(max(count_elements))
    print(data_sorted[index_max])
