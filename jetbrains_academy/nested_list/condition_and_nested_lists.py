# This is a list of students and their grades for an exam:
#
# students = [["Will", "B"], ["Kate", "B"], ["Max", "A"], ["Elsa", "C"], ["Alex", "B"], ["Chris", "A"]]
#
# Select only students with the best grade ("A") and print their names in a list.
# Do all this in one line.

if __name__ == '__main__':
    students = [["Will", "B"], ["Kate", "B"], ["Max", "A"], ["Elsa", "C"],
                ["Alex", "B"], ["Chris", "A"]]

    print([a_grade_student[0] for a_grade_student in students if a_grade_student[1] == 'A'])
