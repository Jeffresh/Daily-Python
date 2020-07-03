# There is a horizontal row of n cubes. The length of each cube is given.
# You need to create a new vertical pile of cubes. T
# he new pile should follow these directions: if is cube_i on top of cube_j then sideLenght_j >= sideLenght_i

# When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time.
# Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.
from collections import deque

if __name__ == '__main__':
    test_cases_number = int(input())

    for _ in range(test_cases_number):
        cubes_number = int(input())
        cubes_list = list(map(int, input().split()))
        d = deque(cubes_list)
        pile = deque()

        last_cube = max(cubes_list)
        for _ in range(cubes_number):
            cube = d.popleft() if d[0] >= d[-1] else d.pop()
            if cube > last_cube:
                print("No")
                break
            last_cube = cube
        else:
            print("Yes")




