# Task
#
# You are given a date. Your task is to find what the day is on that date.

# Input Format
#
# A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY
# format.

import calendar

if __name__ == '__main__':
    DAYS = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    month, day, year = map(int, input().split())
    print(DAYS[calendar.weekday(year, month, day)])
