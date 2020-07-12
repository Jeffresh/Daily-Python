# Neo has a complex matrix script. The matrix script is a N X M grid of strings.
# It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

# To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them.
# Neo reads the column from top to bottom and starts reading from the leftmost column.
#
# If there are symbols or spaces between two alphanumeric characters of the decoded script,
# then Neo replaces them with a single space '' for better readability.
#
# Neo feels that there is no need to use 'if' conditions for decoding.
#
# Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

# Input Format
#
# The first line contains space-separated integers N(rows) and M(columns) respectively.
# The next lines contain the row elements of the matrix script.


import re

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    matrix = []

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)
    print(re.sub(r'(\w)(\W)+(\w)', r'\1 \3', ''.join([u for t in zip(*matrix) for u in t])))
