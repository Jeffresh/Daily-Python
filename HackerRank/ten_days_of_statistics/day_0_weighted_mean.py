# Task
# Given an array, , of integers and an array, ,
# representing the respective weights of 's elements, calculate and print the weighted mean of 's elements.
# Your answer should be rounded to a scale of decimal place (i.e., format).

if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    weight = list(map(int, input().split()))
    numerator = [x * y for x, y in zip(data, weight)]
    print('{0:.1f}'.format(sum(numerator) / sum(weight)))
