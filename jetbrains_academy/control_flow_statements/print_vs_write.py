# There are several ways to write data to a file. Pick the one you find easier and write a list of
# numbers into the file_with_list.txt.
#
# The list with numbers is defined below. Please write the whole list including brackets and don't add a
# newline character \n to the end of the file.


if __name__ == '__main__':
    number = [1234, 5678, 90]
    file = open("file_with_list.txt", 'w')
    print(number, end='', file=file)
    file.close()