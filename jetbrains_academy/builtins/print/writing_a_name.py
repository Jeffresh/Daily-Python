# You are given a list containing letters of a name. Print them out as a string with these chars
# separated by hyphens and with an exclamation point in the end. Do so using arguments of the print() function!
#
# So, if the letters in the list name are ['K', 'A', 'T', 'E'], your program should print the string 'K-A-T-E!'

if __name__ == '__main__':
    name = ['M', 'A', 'R', 'C', 'O']
    print(*name, sep='-', end='!')