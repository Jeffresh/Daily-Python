# Imagine that suddenly all machines have gone insane and simple multiplication is not working for natural
# numbers anymore. Let's write a new function for this task recursively!
#
# It's known that "a times b" is the same thing as "a plus itself b times". So we can rewrite the
# expression in the following way:
#
# a∗b=a+a+a+a+...+aa*b = a + a+ a + a + ... + aa∗b=a+a+a+a+...+a
#
# We need to reduce this problem to a smaller one with the recursive step, and then stop recursion with the base step.
#
# Modify the template code below into a working function that takes two positive integers as its input
# and returns their product.

def multiply(a, b):
    if b == 1:  # base case
        return a
    # recursive case
    return a + multiply(a, b - 1)


if __name__ == '__main__':
    print(multiply(3, 5))
