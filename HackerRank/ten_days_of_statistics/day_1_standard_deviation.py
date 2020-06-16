# Task
# Given an array, , of integers, calculate and print the standard deviation. Your answer should be in decimal form,
# rounded to a scale of decimal place (i.e., format). An error margin of will be tolerated for the standard deviation.


from math import sqrt

if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))

    mean = sum(data) / n

    square_distances = [(mean - x) ** 2 for x in data]

    variance = sum(square_distances) / n
    std = sqrt(variance)
    print('{0:.1f}'.format(std))
