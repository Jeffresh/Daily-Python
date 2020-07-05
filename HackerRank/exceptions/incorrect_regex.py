# You are given a string S.
# Your task is to find out whether S is a valid regex or not.

# Input Format
#
# The first line contains integer T the number of test cases.
# The next T lines contains the string S .

import re

if __name__ == '__main__':

    for _ in range(int(input())):
        ans = True
        try:
            reg = re.compile(input())
        except re.error:
            ans = False
        print(ans)
