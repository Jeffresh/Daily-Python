# Read a string from the input and print a list of vowels that belong to that string.
#
# All vowels are enlisted in a variable of the same name.

if __name__ == '__main__':
    vowels = 'aeiou'
    string = input()
    print([v for v in string if v in vowels])
