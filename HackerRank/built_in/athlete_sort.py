# You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on).
# You are required to sort the data based on the Kth attribute and print the final resulting table.
# Follow the example given below for better understanding.
# Note that is indexed from 0 to M-1 , where M is the number of attributes.


# Input Format
#
# The first line contains N and M and separated by a space.
# The next N lines each contain M elements.
# The last line contains K.

if __name__ == '__main__':
    n, m = map(int, input().split())
    scores = [list(map(int, input().rstrip().split())) for _ in range(n)]
    k = int(input())
    scores_sorted = sorted(scores, key=lambda x: x[k])

    for row in scores_sorted:
        print(*row)
