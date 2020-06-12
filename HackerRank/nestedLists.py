# Given the names and grades
# for each student in a Physics class of students,
# store them in a nested list and print the name(s) of any
# student(s) having the second lowest grade.

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    m = min(students, key=lambda x: x[1])
    students = [x for x in students if x[1] != m[1]]

    m = min(students, key=lambda x: x[1])
    students.sort(key=lambda x: x[1])

    seconds_grade = [x[0] for x in students if x[1] == m[1]]
    seconds_grade.sort()
    for student in seconds_grade:
        print(student)
