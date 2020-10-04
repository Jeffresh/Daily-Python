# Write a function equation_writing() that will print hte equation in the following format: a x + b = c.
# The function must take three arguments: a, b, c, these values are subject to change. The rest of the equation
# remains unchanged.

# You are NOT supposed to handle input or calla function, just implement it.

def equation_writing(a, b, c):
    print(f'{a} x + {b} = {c}')


if __name__ == '__main__':
    equation_writing(3, 4, 3)
