from itertools import groupby

if __name__ == '__main__':

    string = input()
    for i,j in groupby(string):
        print((len(list(j)), int(i)), end=" ")