# Write a program that reads integer from the console, one number per line
# For each input number you should check:
#
# - if the number is less than 10, then skip this number;
# - if the number is greater than 100, then stop reading numbers from the console;
# - in other cases, print this number back to the console on a separate line.

if __name__ == '__main__':

    number = int(input())

    while number >= 100:
        if number >= 10:
            print(number)
        number = int(input())
