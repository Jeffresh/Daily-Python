# Read a string with digits from the input and convert each number to an integer.
# For your newly created list, calculate the running average according to the following formula:
#
# Ai=xi+xi+12,A_i = \frac{x_i + x_{i+1}}{2},Ai​=2xi​+xi+1​​,
# where xix_ixi​ and xi+1x_{i+1}xi+1​ are elements of
# the original list, AiA_iAi​ is the element of the moving average.
#
# Print the result. Notice that this list will have one less item.

if __name__ == '__main__':
    number_list = list(input())

    print([(int(number_list[i]) + int(number_list[i + 1])) / 2 for i in range(len(number_list) - 1)])
