# You are given the file test.txt. Read it and print the first letter from each line.
# Don't forget to close the file!

if __name__ == '__main__':
    # read test.txt
    file = open('test.txt', mode='r')

    for line in file:
        print(line[0])

    file.close()
