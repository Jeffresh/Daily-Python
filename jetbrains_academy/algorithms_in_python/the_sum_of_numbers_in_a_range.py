# Your task here is to implement a simple algorithm that counts the sum of those numbers from a list that belong to a
# specified range.
#
# Input: the first line contains a list of integer numbers separated by spaces. The second line contains two integer
# numbers aaa and bbb such that a≤ba \le ba≤b. The numbers are separated by a space as well. They represent the range.
#
# Output: the sum of all elements xxx of the list such that a≤x≤ba \le x \le ba≤x≤b.
# If the list doesn't contain elements belonging to the specified range, output 000. See the example for more details.


def range_sum(numbers, start, end):
    sum_value = 0
    if numbers:
        for value in numbers:
            if start <= value <= end:
                sum_value += value

    return sum_value


if __name__ == '__main__':
    input_numbers = list(map(int, input().split()))
    a, b = list(map(int, input().split()))
    print(range_sum(input_numbers, a, b))
