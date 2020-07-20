# Read a date from the input given in the following format: YYYY-MM-DD. Print the year, month and day on separate lines.
#
# Sample Input 1:
#
# 2020-04-30
#
# Sample Output 1
#
# 2020
# 04
# 30

if __name__ == '__main__':
    date_list = input().split('-')
    date_string = '\n'.join(date_list)
    print(date_string)
