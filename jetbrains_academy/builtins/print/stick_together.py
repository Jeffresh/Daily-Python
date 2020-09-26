# # you are given a list of numbers. Print them out together.
#
# sample input 1:
#
# 1 2 3 4 5 6...
#
# Sample output 1:
#
# 123456...

if __name__ == '__main__':
    numbers = [int(x) for x in input.split()]
    print(*numbers, sep='')