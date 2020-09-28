# Create 10 files, named file1.txt, file2.txt and so on till file10.txt. The files should contain
# the number corresponding to their name. So, file1.txt should contain one line with number 1, file2.txt -
# one line with number 2 and so on.

if __name__ == '__main__':

    for i in range(1, 11):
        with open('file{}.txt'.format(i), mode='w') as file:
            file.write(str(i))
