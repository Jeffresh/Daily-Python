# Given a numeric sequence at the input, create a list in
# which each number will be a digit from this input string.
# Then use this list to calculate the arithmetic mean, that is, the sum
# of all the digits divided by their total count.

if __name__ == '__main__':
    numbers = [float(x) for x in input()]
    print(sum(numbers) / len(numbers))
