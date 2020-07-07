# You have to generate a list of the first N fibonacci numbers, 0 being the first number.
# Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

# Input Format
#
# One line of input: N an integer


if __name__ == '__main__':
    cube = lambda x: x ** 3  # complete the lambda function


    def fibonacci(n):
        fib = [0, 1]
        for i in range(n - 2):
            fib = fib + [fib[i] + fib[i + 1]]

        return fib[0:n]
        # return a list of fibonacci numbers


    if __name__ == '__main__':
        n = int(input())
        print(list(map(cube, fibonacci(n))))
