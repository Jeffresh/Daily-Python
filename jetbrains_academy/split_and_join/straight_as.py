# Write a program that calculates the proportion of students who received grade A.
#
# A five-point rating system with grades A, B, C, D, F is used.
#
# Input format:
# A string with students' marks separated by space. At least one mark will be present.
#
# Output format:
# A fractional number with exactly two decimal places.
#
# To format the decimal places use the round(number, places) function.

if __name__ == '__main__':
    grades = input().split()
    print(round(grades.count('A') / len(grades), 2))
