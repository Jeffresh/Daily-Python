# In math, we call a natural number prime if it's greater than 1 and can be evenly divided only by 1
# and itself (without any remainder):
#
# 2, 3, 5, 7, 11, 13, 17, ...
#
# Create a list of all primes up to 1000 in the code below. Just save this list into a variable
# prime_numbers, you don't have to print anything.
#
# Make use of any() or all() to check if a number n leaves a zero remainder when divided by values
# from 2 to n - 1 (inclusively).

if __name__ == '__main__':
    prime_numbers = [x for x in range(2, 100) if (x % i for i in range(2, x))]
