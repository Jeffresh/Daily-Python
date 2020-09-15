# The code below solves the following problem — having the numerator and the denominator of a fraction,
# check if the fraction equals 0.5. The program should print True or False. If the denominator equals 0,
# the answer is False.

def compare(numerator, denominator):
    return bool(denominator and numerator / denominator == 0.5)


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(compare(a, b))
