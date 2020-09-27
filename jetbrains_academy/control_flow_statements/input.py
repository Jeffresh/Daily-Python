# Read a line from input and write it to the file input.txt.


if __name__ == '__main__':
    # write the code here
    line = input()
    file = open('input.txt', mode='w')
    file.write(line)
    file.close()
