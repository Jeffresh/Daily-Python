# The Fibonacci numbers (denoted FnF_{n}Fn​) form a sequence where each number is the sum of the two preceding
# ones: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
#
# Fn=Fn−1+Fn−2F_{n} = F_{n-1} + F_{n-2} Fn​=Fn−1​+Fn−2​ , and F0=0,F1=1F_0 = 0, F_1 = 1F0​=0,F1​=1

# The Fibonacci numbers were used to illustrate the growth of an idealized rabbit population that live and
# reproduce according to the following rules:
#
#     the initial population is a pair of baby rabbits (a female + a male)
#     rabbits become adults at the age of one month and after another month give birth to a new pair of baby rabbits
#     these rabbits are immortal
#     a pair of adult rabbits always gives birth to one new pair (a female + a male) a month


def fib(n):
    if n == 0:  # base case for month 0
        return 0  # the rabbits are not on a farm yet!
    elif n == 1:  # base case for month 1
        return 1  # a pair of baby rabbit has just arrived!
    else:
        return fib(n - 1) + fib(n - 2)  # recursive calls


if __name__ == '__main__':
    print(fib(7))
