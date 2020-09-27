# You have the file sums.txt. It has multiple lines that contain two numbers separated by whitespace. All numbers are
# positive.

# For example:
# 9 61
# 15 47
# 2 1

# Write a program tha treads this file and print the sum of number son each line. So, if the files has
# n lines, you should print n sums, each on a separate line.

# Don't forget to close the file!

if __name__ == '__main__':
    # read sums.txt
    file = open('sums.txt', mode='r')
    for line in file:
        a, b = line.split()
        print(int(a) + int(b))

    file.close()