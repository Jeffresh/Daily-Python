# Read the file sample.txt and print the number of lines that this file has.
# Don't forget to close the file!


if __name__ == '__main__':
    file = open('sample.txt', 'r')
    print(len((file.readlines())))
    file.close()
