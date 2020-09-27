# As you have learned, the print() function is an alternative to the file.write() function.
# Now, let's write to a file "A string to be written to a file!" using the print() function.
#
# The file name to use is "test.txt", and all next steps you should perform by yourself.


if __name__ == '__main__':
    f_name = "test.txt"
    my_string = "A string to be written to a file!"

    file_opened = open(f_name, mode='w')
    print(my_string, file=file_opened)
    file_opened.close()
