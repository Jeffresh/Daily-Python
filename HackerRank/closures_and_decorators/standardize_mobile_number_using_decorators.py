# Let's dive into decorators! You are given N
# mobile numbers. Sort them in ascending order then print them in the standard format shown below:
#
# +91 xxxxx xxxxx
#

# Input Format
#
# The first line of input contains an integer N the number of mobile phone numbers.
# N lines follow each containing a mobile number.


def wrapper(f):
    def fun(l):
        f(f'+91 {phone[-10:-5]} {phone[-5:]}' for phone in l)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
