# there is a file called test_file.txt. Read this file and print the first line. Specify encoding=utf-16
# Don't forget to close the file!

if __name__ == '__main__':
    file = open('test_file.txt', mode='r', encoding='utf-16')
    print(file.readline())
    file.close()