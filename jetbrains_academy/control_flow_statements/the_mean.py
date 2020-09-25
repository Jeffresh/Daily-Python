# Calculate the arithmetic mean of integer numbers. You will receive the integers on separate lines. The
# numeric sequence ends with a period ., so stop

def mean(numbers):
    input_value = input()

    if input_value == '.':
        return sum(numbers) / len(numbers)
    else:
        numbers.append(int(input_value))
        return mean(numbers)


if __name__ == '__main__':
    print(mean([]))
