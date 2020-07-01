# Task
#
# Dr. John Wesley has a spreadsheet containing a list of student's ID, marks, class and name
# Your task is to help Dr. Wesley calculate the average marks of the students.
# average = Sum of all marks / total students
from collections import namedtuple

if __name__ == '__main__':
    n_students = int(input())
    column_names = input()
    score = 0
    Student = namedtuple('Student', column_names)
    for _ in range(n_students):
        student = Student(*input().split())
        score += int(student.MARKS)
    print('{:.2f}'.format(score / n_students))

