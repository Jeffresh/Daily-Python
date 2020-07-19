# Print a list of numbers from 1 to 1000 that can be divided by 3

if __name__ == '__main__':
    print([x for x in range(1, 1001) if x % 3 == 0])
