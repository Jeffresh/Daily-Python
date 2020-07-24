# It's impossible not to know the dice game. Please, write a program that will imitate a roll
# of one of the dice with the help of an appropriate random function.
#
# Thus, your task is just to generate one integer in the range from 1 to 6 and print it.


import random

if __name__ == '__main__':
    random.seed(int(input()))
    print(random.randint(1, 6))
