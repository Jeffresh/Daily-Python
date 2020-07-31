# In the code template below you can see two functions that represent different mathematic processes.
# However, there is a line of code repeated in both these functions. Since this part of code does the same
# thing in both functions, it can be moved from these functions into another separate function.
#
# Find this line of code and create a function with it. Name this function common_part.
#
# You do NOT need to work with the input or call any functions.


def calculate_linear(k, b, x):
    y = k * x + b
    common_part(y)


def calculate_quadratic(a, b, c, x):
    y = (a * x * x) + (b * x) + c
    common_part(y)


def common_part(y):
    print("Value of the function equals", y)
    return y


if __name__ == '__main__':
    calculate_linear(4, 6, 7)
    calculate_quadratic(4, 5, 7, 1)
