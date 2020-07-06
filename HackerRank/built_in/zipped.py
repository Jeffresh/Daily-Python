# Task
#
# The National University conducts an examination of N students in X subjects.
# Your task is to compute the average scores of each student.

# Input Format
# The first line contains and separated by a space.
# The next lines contains the space separated marks obtained by students in a particular subject.

if __name__ == '__main__':
    n, x = map(int, input().split())
    scores = [map(float, input().split()) for _ in range(x)]

    [print(sum(student) / x) for student in zip(*scores)]
