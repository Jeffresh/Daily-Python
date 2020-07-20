# Draw a triangle of a given height, as in the example.

if __name__ == '__main__':
    height = int(input())
    structure = [('#' * (i * 2 + 1)).center(height * 2 - 1) for i in range(height)]
    print(*structure, sep='\n')
